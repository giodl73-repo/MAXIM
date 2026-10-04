"""Build MAXIM's search entries from the built site's authoritative MkDocs index.

Run after mkdocs build, then feed entries.json to the native maxim-index binary.
Only numbered, published guide pages are included, never hidden governance files.
"""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def plain(text):
    parser = PlainText()
    parser.feed(text)
    return " ".join(" ".join(parser.parts).split())


def entries_from_docs(docs, site):
    entries = []
    seen = set()
    for doc in docs:
        location = doc["location"]
        url = urlsplit(location)
        parts = unquote(url.path).strip("/").split("/")
        if (url.scheme or url.netloc or location.startswith("/") or ".." in parts
                or len(parts) != 2 or not re.match(r"^\d{2}-", parts[1])
                or not re.fullmatch(r"[a-z][a-z0-9-]*", parts[0])):
            continue
        target = site / unquote(url.path)
        if not target.suffix:
            target = target / "index.html"
        if not target.is_file():
            raise ValueError(f"Search entry has no rendered guide: {location}")
        if location in seen:
            continue
        seen.add(location)
        entries.append({"title": plain(doc["title"]), "url": location,
                        "section": parts[0], "text": plain(doc["text"])})
    return sorted(entries, key=lambda entry: entry["url"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument("--output", type=Path, help="Optional entries JSON destination")
    args = parser.parse_args()
    source = args.site / "search/search_index.json"
    entries = entries_from_docs(json.loads(source.read_text(encoding="utf-8"))["docs"], args.site)
    if not entries:
        raise ValueError("No published numbered guide entries found")
    destination = args.output or args.site / "explore/entries.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(entries, ensure_ascii=False), encoding="utf-8")
    print(f"Prepared {len(entries)} entries across {len({e['section'] for e in entries})} modules")


if __name__ == "__main__":
    main()
