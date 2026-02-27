"""
Build a world map SVG using Natural Earth 110m land polygons.
Generates a complete inline SVG with the atlas light/warm style.

Two output modes:
  --full     All polygons with area > 0.5 (for geographic reference maps)
  --context  Polygons with area > 10 only (for thematic overlays)

Output: SVG to stdout (paste into markdown files)
"""

import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon
import argparse
import sys


def geom_to_svg_d(geom, precision=1):
    """Convert a Shapely geometry to SVG path d attribute string."""
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
    parser.add_argument("--mode", choices=["full", "context"], default="full")
    parser.add_argument("--min-area", type=float, default=None)
    parser.add_argument("--stroke-width", type=float, default=0.4)
    parser.add_argument("--precision", type=int, default=1,
                       help="Decimal places for coordinates")
    args = parser.parse_args()

    if args.min_area is None:
        args.min_area = 0.5 if args.mode == "full" else 10.0

    gdf = gpd.read_file("ne_110m_land.shp")

    # Collect all polygons above area threshold
    all_paths = []
    for idx, row in gdf.iterrows():
        geom = row.geometry
        if isinstance(geom, Polygon):
            if geom.area >= args.min_area:
                all_paths.extend(geom_to_svg_d(geom, args.precision))
        elif isinstance(geom, MultiPolygon):
            for g in geom.geoms:
                if g.area >= args.min_area:
                    all_paths.extend(geom_to_svg_d(Polygon(g.exterior), args.precision))

    # Output SVG paths with atlas styling
    sw = args.stroke_width
    fill = "#e8e4dc" if args.mode == "full" else "none"
    stroke_color = "#444" if args.mode == "full" else "#ccc"

    print(f"  <!-- Natural Earth 110m land — {len(all_paths)} polygons, "
          f"min_area={args.min_area} -->")

    for d in all_paths:
        print(f'  <path d="{d}"')
        print(f'        fill="{fill}" stroke="{stroke_color}" '
              f'stroke-width="{sw}" stroke-linejoin="round"/>')


if __name__ == "__main__":
    main()
