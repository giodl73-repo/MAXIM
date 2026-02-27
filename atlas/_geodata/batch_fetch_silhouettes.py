"""
Batch-fetch organism silhouettes from PhyloPic.
Downloads SVG source files for all organisms needed across the 52 atlas maps.
Saves to atlas/_geodata/silhouettes/ with standardized filenames.
Tracks licenses for attribution.
"""

import json
import urllib.request
import urllib.parse
import os
import sys
import time

API = "https://api.phylopic.org"
BUILD = 535
OUT_DIR = "silhouettes"

# All organisms to fetch, grouped by atlas map
ORGANISMS = {
    # Map 05: Global Biomes
    "cactus": "cactus",
    "palm": "palm trees",
    "conifer": "conifers",
    "fern": "ferns",
    "moss": "moss",
    "mangrove": "mangrove",

    # Map 07: Grain & Fermentation
    "wheat": "wheat",
    "rice": "rice",
    "maize": "maize",
    "barley": "barley",
    "grape": "grapes",
    "coffee": "coffee",

    # Map 08: Flyways & Migration (some already downloaded)
    "albatross": "albatrosses",
    "crane": "cranes",
    "flamingo": "flamingo",
    "pelican": "pelicans",
    "eagle": "eagles",
    "penguin": "penguin",
    "sea_turtle": "sea turtles",
    "salmon": "salmon",
    "wildebeest": "wildebeests",
    "caribou": "caribou",

    # Map 09: Medicinal Plants
    "poppy": "poppy",
    "aloe": "aloe",
    "cannabis": "cannabis",

    # Map 10: Disease Vectors
    "mosquito": "mosquito",
    "tick": "ticks",
    "flea": "fleas",
    "rat": "rats",

    # Map 11: Biodiversity Hotspots
    "orangutan": "orangutans",
    "tiger": "tiger",
    "panda": "panda",
    "lemur": "lemur",
    "toucan": "toucans",
    "jaguar": "jaguar",
    "elephant": "elephant",
    "rhinoceros": "rhinoceros",
    "gorilla": "gorilla",
    "koala": "koala",

    # Map 12: Human Migration
    "homo_sapiens": "homo sapiens",

    # Map 15: Forest Types
    "oak": "oaks",
    "spruce": "spruces",
    "eucalyptus": "eucalyptus",
    "bamboo": "bamboos",
    "baobab": "baobab",

    # Map 16: Fiber Crops
    "sheep": "sheep",
    "llama": "llama",
    "silkworm": "silkworms",

    # General / cross-map
    "fish": "fishes",
    "coral": "corals",
    "mushroom": "mushrooms",
    "bee": "bees",
    "ant": "ants",
    "crocodile": "crocodiles",
    "snake": "snake",
    "frog": "frogs",
    "lizard": "lizards",
    "shark": "sharks",
    "dolphin": "dolphin",
    "horse": "horse",
    "cow": "cattle",
    "pig": "pig",
    "chicken": "chicken",
    "dog": "dog",
    "cat": "cat",
}


def find_node_uuid(name):
    """Find taxonomic node UUID by name."""
    url = f"{API}/nodes?build={BUILD}&filter_name={urllib.parse.quote(name)}&page=0&embed_items=true"
    with urllib.request.urlopen(url, timeout=10) as resp:
        data = json.loads(resp.read())
    items = data.get("_embedded", {}).get("items", [])
    if not items:
        return None
    href = items[0]["_links"]["self"]["href"]
    return href.split("/nodes/")[1].split("?")[0]


def get_best_svg_image(node_uuid):
    """Get the best SVG image for a clade. Prefers CC0, then CC-BY."""
    url = f"{API}/images?build={BUILD}&filter_clade={node_uuid}&page=0&embed_items=true"
    with urllib.request.urlopen(url, timeout=10) as resp:
        data = json.loads(resp.read())

    items = data.get("_embedded", {}).get("items", [])

    svg_images = []
    for img in items:
        links = img.get("_links", {})
        source = links.get("sourceFile", {})
        if source.get("type") != "image/svg+xml":
            continue

        license_url = links.get("license", {}).get("href", "")
        species = links.get("specificNode", {}).get("title", "unknown")
        uuid = links["self"]["href"].split("/images/")[1].split("?")[0]

        # Score: CC0 > CC-BY > CC-BY-SA
        if "zero" in license_url or "publicdomain" in license_url:
            score = 3
        elif "by/4" in license_url or "by/3" in license_url:
            score = 2
        elif "by-sa" in license_url:
            score = 1
        else:
            score = 0

        svg_images.append({
            "uuid": uuid,
            "species": species,
            "license": license_url,
            "svg_url": source["href"],
            "score": score,
        })

    if not svg_images:
        return None

    # Return best-licensed image
    svg_images.sort(key=lambda x: -x["score"])
    return svg_images[0]


def download_svg(url, filepath):
    """Download SVG file."""
    with urllib.request.urlopen(url, timeout=15) as resp:
        data = resp.read()
    with open(filepath, "wb") as f:
        f.write(data)
    return len(data)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    # Track results
    success = []
    failed = []
    skipped = []

    # License manifest for attribution
    manifest = []

    total = len(ORGANISMS)
    for i, (key, search_name) in enumerate(ORGANISMS.items()):
        filepath = os.path.join(OUT_DIR, f"{key}.svg")

        # Skip if already downloaded
        if os.path.exists(filepath) and os.path.getsize(filepath) > 100:
            skipped.append(key)
            print(f"  [{i+1}/{total}] {key:20s} SKIP (already exists)")
            continue

        try:
            # Find node
            uuid = find_node_uuid(search_name)
            if not uuid:
                failed.append((key, "no node found"))
                print(f"  [{i+1}/{total}] {key:20s} FAIL (no node for '{search_name}')")
                continue

            # Get best SVG
            img = get_best_svg_image(uuid)
            if not img:
                failed.append((key, "no SVG image"))
                print(f"  [{i+1}/{total}] {key:20s} FAIL (no SVG image)")
                continue

            # Download
            size = download_svg(img["svg_url"], filepath)
            success.append(key)
            manifest.append({
                "key": key,
                "species": img["species"],
                "license": img["license"],
                "uuid": img["uuid"],
            })
            lic_short = "CC0" if "zero" in img["license"] else "CC-BY" if "by/" in img["license"] else "other"
            print(f"  [{i+1}/{total}] {key:20s} OK   {img['species']:30s} {lic_short:6s} {size:6d}B")

            time.sleep(0.3)  # rate limit courtesy

        except Exception as e:
            failed.append((key, str(e)))
            print(f"  [{i+1}/{total}] {key:20s} ERR  {e}")

    # Save manifest
    manifest_path = os.path.join(OUT_DIR, "_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    # Summary
    print(f"\n{'='*60}")
    print(f"BATCH COMPLETE")
    print(f"  Downloaded: {len(success)}")
    print(f"  Skipped:    {len(skipped)}")
    print(f"  Failed:     {len(failed)}")
    if failed:
        print(f"\n  Failed organisms:")
        for key, reason in failed:
            print(f"    {key}: {reason}")
    print(f"\n  Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
