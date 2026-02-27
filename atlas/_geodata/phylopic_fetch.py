"""
Fetch organism silhouettes from PhyloPic API.
Downloads SVG source files and extracts the <path> data for inline embedding.

Usage:
    python phylopic_fetch.py "arctic tern"
    python phylopic_fetch.py "whale" --save whale.svg
    python phylopic_fetch.py "monarch butterfly" --list  # show all matches
"""

import argparse
import json
import urllib.request
import sys
import re
import os

API = "https://api.phylopic.org"
BUILD = 535


def autocomplete(query):
    """Get name matches for a query."""
    url = f"{API}/autocomplete?build={BUILD}&query={urllib.parse.quote(query)}"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read())
    return data.get("matches", [])


def find_node(name):
    """Find a taxonomic node by exact name."""
    url = f"{API}/nodes?build={BUILD}&filter_name={urllib.parse.quote(name)}&page=0&embed_items=true"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read())
    items = data.get("_embedded", {}).get("items", [])
    if not items:
        return None
    return items[0]


def get_clade_images(node_uuid, limit=5):
    """Get silhouette images for a clade."""
    url = f"{API}/images?build={BUILD}&filter_clade={node_uuid}&page=0&embed_items=true"
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read())
    return data.get("_embedded", {}).get("items", [])[:limit]


def get_node_images(name):
    """Search by name, find node, get images."""
    # Try autocomplete first
    matches = autocomplete(name)
    if not matches:
        print(f"No matches for '{name}'", file=sys.stderr)
        return []

    # Try exact match first, then first match
    target = name.lower()
    exact = [m for m in matches if m.lower() == target]
    chosen = exact[0] if exact else matches[0]

    print(f"Using: {chosen}", file=sys.stderr)

    node = find_node(chosen)
    if not node:
        print(f"No node found for '{chosen}'", file=sys.stderr)
        return []

    uuid = node["_links"]["self"]["href"].split("/nodes/")[1].split("?")[0]
    images = get_clade_images(uuid)

    results = []
    for img in images:
        links = img.get("_links", {})
        source = links.get("sourceFile", {})
        specific = links.get("specificNode", {})
        license_link = links.get("license", {})

        if source.get("type") == "image/svg+xml":
            results.append({
                "name": specific.get("title", "unknown"),
                "svg_url": source["href"],
                "license": license_link.get("href", "unknown"),
                "uuid": links["self"]["href"].split("/images/")[1].split("?")[0],
            })

    return results


def download_svg(url):
    """Download an SVG file and return its content."""
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode("utf-8")


def extract_paths(svg_content):
    """Extract all <path> d attributes from SVG content."""
    paths = re.findall(r'<path[^>]*\bd="([^"]*)"', svg_content)
    return paths


def main():
    import urllib.parse

    parser = argparse.ArgumentParser(description="Fetch PhyloPic silhouettes")
    parser.add_argument("query", help="Organism name to search")
    parser.add_argument("--list", action="store_true", help="List matches only")
    parser.add_argument("--save", help="Save SVG to file")
    parser.add_argument("--index", type=int, default=0, help="Which result to use (0-based)")
    args = parser.parse_args()

    if args.list:
        matches = autocomplete(args.query)
        for m in matches:
            print(f"  {m}")
        return

    results = get_node_images(args.query)
    if not results:
        print("No SVG images found.")
        return

    print(f"\nFound {len(results)} SVG silhouettes:", file=sys.stderr)
    for i, r in enumerate(results):
        marker = "→" if i == args.index else " "
        print(f"  {marker} [{i}] {r['name']} — {r['license']}", file=sys.stderr)

    chosen = results[min(args.index, len(results)-1)]
    print(f"\nDownloading: {chosen['name']}", file=sys.stderr)
    print(f"License: {chosen['license']}", file=sys.stderr)
    print(f"URL: {chosen['svg_url']}", file=sys.stderr)

    svg = download_svg(chosen["svg_url"])

    if args.save:
        with open(args.save, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"Saved to {args.save}", file=sys.stderr)
    else:
        # Extract paths and output for inline use
        paths = extract_paths(svg)
        print(f"\n{len(paths)} path(s) extracted:", file=sys.stderr)
        viewbox = re.search(r'viewBox="([^"]*)"', svg)
        if viewbox:
            print(f"viewBox: {viewbox.group(1)}", file=sys.stderr)
        print()
        for p in paths:
            print(f'd="{p}"')


if __name__ == "__main__":
    main()
