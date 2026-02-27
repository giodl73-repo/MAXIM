"""
Extract continent coastline paths from Natural Earth 110m land polygons.
Outputs SVG <path> elements using equirectangular projection:
  x = longitude (positive east)
  y = -latitude (north is negative, SVG y-axis points down)

This matches the atlas world map coordinate convention.
"""

import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon
import sys

def geom_to_svg_path(geom, min_area=0):
    """Convert a Shapely geometry to SVG path d attribute.
    x = longitude, y = -latitude (flip for SVG)."""
    paths = []

    if isinstance(geom, Polygon):
        polys = [geom]
    elif isinstance(geom, MultiPolygon):
        polys = list(geom.geoms)
    else:
        return ""

    for poly in polys:
        if poly.area < min_area:
            continue
        coords = list(poly.exterior.coords)
        if len(coords) < 3:
            continue
        # Build SVG path: M start L points Z
        parts = [f"M{coords[0][0]:.1f},{-coords[0][1]:.1f}"]
        for x, y in coords[1:]:
            parts.append(f"L{x:.1f},{-y:.1f}")
        parts.append("Z")
        paths.append(" ".join(parts))

    return "\n".join(paths)


def main():
    gdf = gpd.read_file("ne_110m_land.shp")

    print(f"<!-- Natural Earth 110m land polygons — public domain -->")
    print(f"<!-- {len(gdf)} features, equirectangular projection -->")
    print(f"<!-- x = longitude, y = -latitude -->\n")

    # For world maps, we want all land. Skip tiny islands (area < 1 sq degree).
    for idx, row in gdf.iterrows():
        geom = row.geometry
        svg_d = geom_to_svg_path(geom, min_area=0.5)
        if svg_d:
            for i, path_d in enumerate(svg_d.split("\n")):
                print(f'<path d="{path_d}"')
                print(f'      fill="#e8e4dc" stroke="#444" stroke-width="0.4" stroke-linejoin="round"/>')
                print()


if __name__ == "__main__":
    main()
