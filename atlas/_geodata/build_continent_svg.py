"""
Extract continent-level coastlines from Natural Earth 110m.
Crops to a bounding box per continent with appropriate viewBox.

Usage:
    python build_continent_svg.py --continent africa
    python build_continent_svg.py --continent europe --mode full
    python build_continent_svg.py --list   # show all continent definitions
"""

import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon, box
import argparse
import sys

# Standard continent bounding boxes: (min_lon, min_lat, max_lon, max_lat)
# Plus recommended SVG dimensions
CONTINENTS = {
    "north_america": {
        "bbox": (-170, 7, -50, 84),
        "width": 900, "height": 580,
        "label": "North America",
    },
    "south_america": {
        "bbox": (-82, -56, -34, 13),
        "width": 700, "height": 600,
        "label": "South America",
    },
    "europe": {
        "bbox": (-12, 34, 45, 72),
        "width": 800, "height": 530,
        "label": "Europe",
    },
    "africa": {
        "bbox": (-20, -36, 52, 38),
        "width": 750, "height": 600,
        "label": "Africa",
    },
    "asia": {
        "bbox": (25, -10, 180, 78),
        "width": 960, "height": 550,
        "label": "Asia",
    },
    "oceania": {
        "bbox": (110, -48, 180, -8),
        "width": 800, "height": 460,
        "label": "Oceania & Australia",
    },
    "middle_east": {
        "bbox": (24, 12, 64, 42),
        "width": 800, "height": 480,
        "label": "Middle East",
    },
    "southeast_asia": {
        "bbox": (90, -12, 155, 30),
        "width": 900, "height": 460,
        "label": "Southeast Asia",
    },
    "caribbean": {
        "bbox": (-90, 10, -58, 28),
        "width": 800, "height": 360,
        "label": "Caribbean",
    },
    "mediterranean": {
        "bbox": (-6, 28, 42, 48),
        "width": 900, "height": 380,
        "label": "Mediterranean",
    },
}


def geom_to_svg_d(geom, precision=1):
    """Convert geometry to SVG path d string, clipped to display area."""
    paths = []
    if isinstance(geom, Polygon):
        polys = [geom]
    elif isinstance(geom, MultiPolygon):
        polys = list(geom.geoms)
    else:
        return []

    for poly in polys:
        coords = list(poly.exterior.coords)
        if len(coords) < 3:
            continue
        fmt = f"{{:.{precision}f}}"
        parts = ["M" + fmt.format(coords[0][0]) + "," + fmt.format(-coords[0][1])]
        for x, y in coords[1:]:
            parts.append("L" + fmt.format(x) + "," + fmt.format(-y))
        parts.append("Z")
        paths.append(" ".join(parts))
    return paths


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--continent", help="Continent name (e.g., 'africa', 'europe')")
    parser.add_argument("--mode", choices=["full", "context"], default="full")
    parser.add_argument("--precision", type=int, default=1)
    parser.add_argument("--list", action="store_true", help="List available continents")
    parser.add_argument("--min-area", type=float, default=0.1,
                       help="Minimum polygon area in square degrees")
    args = parser.parse_args()

    if args.list:
        print("Available continents:")
        for key, conf in CONTINENTS.items():
            bb = conf["bbox"]
            print(f"  {key:20s}  {conf['label']:25s}  "
                  f"bbox=({bb[0]},{bb[1]},{bb[2]},{bb[3]})  "
                  f"{conf['width']}x{conf['height']}")
        return

    if not args.continent or args.continent not in CONTINENTS:
        print(f"Unknown continent: {args.continent}", file=sys.stderr)
        print(f"Available: {', '.join(CONTINENTS.keys())}", file=sys.stderr)
        sys.exit(1)

    conf = CONTINENTS[args.continent]
    min_lon, min_lat, max_lon, max_lat = conf["bbox"]

    # Build clipping box
    clip_box = box(min_lon, min_lat, max_lon, max_lat)

    # ViewBox: x = min_lon, y = -max_lat, width = lon range, height = lat range
    vb_x = min_lon
    vb_y = -max_lat
    vb_w = max_lon - min_lon
    vb_h = max_lat - min_lat

    gdf = gpd.read_file("ne_110m_land.shp")

    # Clip and collect paths
    all_paths = []
    for idx, row in gdf.iterrows():
        geom = row.geometry
        clipped = geom.intersection(clip_box)
        if clipped.is_empty:
            continue

        if isinstance(clipped, Polygon):
            polys = [clipped]
        elif isinstance(clipped, MultiPolygon):
            polys = list(clipped.geoms)
        else:
            continue

        for p in polys:
            if p.area >= args.min_area:
                all_paths.extend(geom_to_svg_d(p, args.precision))

    # Output
    fill = "#e8e4dc" if args.mode == "full" else "none"
    stroke = "#444" if args.mode == "full" else "#ccc"
    sw = 0.15 if args.mode == "full" else 0.1

    print(f"  <!-- Natural Earth 110m -- {conf['label']} -- {len(all_paths)} polygons -->")
    for d in all_paths:
        print(f'  <path d="{d}"')
        print(f'        fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>')


if __name__ == "__main__":
    main()
