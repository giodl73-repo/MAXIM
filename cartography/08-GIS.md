# 08 — GIS: Geographic Information Systems

## Maps Become Computable

GIS is the transition from maps as artifacts to maps as queryable databases. Before GIS, a map was a drawing — you could look at it, trace it, but you couldn't ask it questions. With GIS, geographic data is stored in structures that support spatial queries: give me all the parcels within 500m of this flood zone, show me the areas where population density exceeds 1,000/km² and income is below the poverty line, find the shortest route from here to there.

```
GIS CONCEPTUAL STACK
══════════════════════════════════════════════════════════════════════

  USER QUESTION:
  "Show me all hospitals within 10km of the earthquake epicenter"

  ↓ GIS PROCESSING:

  1. SPATIAL DATA:
     - Hospital point layer (geometry + attributes)
     - Earthquake epicenter (point)
     - Administrative boundary (polygon)

  2. SPATIAL OPERATION:
     Buffer(epicenter, 10km) → circular polygon
     SpatialJoin(hospitals, buffer) → hospitals inside buffer
     Select(result, "status = 'open'") → operating hospitals

  3. RESULT:
     List of hospitals + distance from epicenter + capacity

  ↓ OUTPUT:

  MAP + TABLE + REPORT

  ─────────────────────────────────────────────────────────────

  GIS IS: spatial database + spatial analysis engine + renderer

  GIS is NOT: just mapping software (though it does that)
              just GPS navigation (though it includes that)
              just pretty pictures (though it makes those)

══════════════════════════════════════════════════════════════════════
```

---

## Roger Tomlinson and the First GIS (1960s)

Roger Tomlinson is the "Father of GIS." His Canada Geographic Information System (CGIS), developed starting in 1963 for the Canada Land Inventory, was the first operational GIS — the first system that treated geographic data as a computable database rather than a paper map.

```
CANADA LAND INVENTORY — THE PROBLEM THAT CREATED GIS
══════════════════════════════════════════════════════════════════════

  THE PROBLEM (1962):
  The Canadian government needed to inventory:
  - 2.5 million km² of rural Canada
  - Multiple themes: soil capability, land use, wildlife,
    forestry, recreation suitability
  - Goal: find the best agricultural land for settlement programs

  THE PAPER MAP APPROACH (what they tried first):
  ├── Map each theme onto paper maps at 1:50,000 scale
  ├── Overlay maps by hand (physical lightbox)
  ├── Measure areas by dot grid or planimeter
  └── PROBLEM: ~10,000 map sheets × 5 themes = 50,000 overlays
      Impossible at that scale to do by hand

  TOMLINSON'S INSIGHT (1963):
  ├── Digitize the maps (scan/encode as computer data)
  ├── Store in structured database
  ├── Overlay by Boolean operations, not by hand
  ├── Measure areas computationally, not with dot grids
  └── Query: "show me all areas with soil class A AND within 10km
      of a road" = database query, not physical map manipulation

  THE RESULT:
  CGIS ran from 1966, fully operational by 1971.
  Completed in years what would have taken decades by hand.
  Tomlinson coined the term "Geographic Information System" in 1968.

══════════════════════════════════════════════════════════════════════
```

The CGIS problem is structurally identical to relational database problems that IBM and others were solving at the same time (Codd's relational model: 1970). The difference: GIS adds a spatial geometry type alongside the relational attributes, and adds a spatial index and query operators. In effect, GIS is SQL plus spatial predicates.

---

## Data Models — Vector vs Raster

The fundamental split in GIS data representation is vector (discrete objects) vs raster (continuous fields).

```
VECTOR DATA MODEL
══════════════════════════════════════════════════════════════════════

  GEOMETRY TYPES:
  ┌──────────────────────────────────────────────────────────┐
  │  POINT: single coordinate pair (x,y) or (x,y,z)         │
  │  Examples: city center, tree location, sensor station    │
  │                                                          │
  │  LINE (LineString): ordered sequence of points           │
  │  Examples: road, river, pipeline, power line             │
  │                                                          │
  │  POLYGON: closed ring of points                          │
  │  Examples: parcel, country boundary, lake, building      │
  │                                                          │
  │  MULTI-variants: MultiPoint, MultiLineString, MultiPolygon│
  │  Example: country with islands = MultiPolygon            │
  │                                                          │
  │  GEOMETRY COLLECTION: mix of types                       │
  │                                                          │
  │  These are the OGC Simple Features standard geometry     │
  │  types — used by PostGIS, GEOS, Shapefile, GeoJSON, KML  │
  └──────────────────────────────────────────────────────────┘

  ATTRIBUTES:
  Each geometry has associated attributes (like database table row):
  Road: {geometry: LineString, name: "I-90", lanes: 6, surface: "asphalt"}
  Parcel: {geometry: Polygon, owner: "Smith", area_sqm: 4500, zoning: "R1"}

  TOPOLOGY:
  Vector data can have topological rules enforced:
  - Polygons must not overlap
  - Road network must be connected at intersections
  - Parcels must cover the entire jurisdiction without gaps
  Topological GIS (traditional ESRI coverage model) was important
  before database constraints; modern GIS uses rules/validation instead.

══════════════════════════════════════════════════════════════════════
```

```
RASTER DATA MODEL
══════════════════════════════════════════════════════════════════════

  STRUCTURE:
  ┌──────────────────────────────────────────────────────────┐
  │  Regular grid of cells (pixels)                          │
  │  Each cell: single value (or multiple bands)             │
  │  Cell size = spatial resolution                          │
  │                                                          │
  │  1m cell: 1 cell = 1m² of Earth surface                 │
  │  30m cell (Landsat): 1 cell = 900m² of Earth            │
  │  1km cell (MODIS): 1 cell = 1km²                        │
  └──────────────────────────────────────────────────────────┘

  COMMON RASTER TYPES:
  ├── DEM (Digital Elevation Model): height per cell
  ├── Satellite imagery: spectral reflectance per band per cell
  ├── Population density: people per km² per cell
  ├── Land cover classification: category code per cell
  └── Interpolated field: rainfall, temperature, pollution

  RASTER MATH:
  Rasters of same extent/resolution can be combined:
  NDVI = (NIR - Red) / (NIR + Red)  → cell-by-cell arithmetic
  Slope = gradient of DEM → surface analysis
  Reclassify: value bins → category codes

══════════════════════════════════════════════════════════════════════
```

### Vector vs Raster — When to Use Which

| Scenario | Vector | Raster |
|----------|--------|--------|
| Road network | Yes — topology matters | Poor — diagonal roads lose precision |
| Administrative boundaries | Yes — parcel accuracy matters | Poor — boundary is a line, not a zone |
| Elevation model | Poor — requires TIN or contour | Yes — natural grid |
| Satellite imagery | Not applicable | Yes — sensor is a grid |
| Land use categories | Both work | Yes — for continuous coverage |
| Population density | Poor — points, not continuous | Yes — interpolated surface |
| Building footprints | Yes — precise polygons | Poor — loses precision |
| Wildfire burn scar | Both work | Yes — from satellite classification |

In practice, GIS workflows combine vector and raster: extract elevation values at road intersections (sample raster at vector points), create flood zones by selecting areas below contour (raster DEM → vector polygon).

---

## Spatial Reference Systems and EPSG Codes

```
COORDINATE REFERENCE SYSTEMS IN GIS
══════════════════════════════════════════════════════════════════════

  Every spatial dataset must declare its CRS.
  Without a CRS, coordinates are meaningless numbers.

  CRS COMPONENTS:
  ├── Datum: which ellipsoid, which origin (WGS84, NAD83, etc.)
  ├── Projection: how coordinates are expressed
  │   Geographic: (latitude, longitude) in degrees
  │   Projected: (easting, northing) in meters or feet
  └── Units: degrees or meters or feet

  EPSG CODES (European Petroleum Survey Group codes):
  Standard integer identifiers for CRS definitions.
  Maintained at epsg.io

  COMMONLY USED:
  ┌──────────────────────────────────────────────────────────┐
  │  EPSG:4326  WGS84 geographic (lat/lon in degrees)        │
  │             Used by GPS, GeoJSON, Google APIs            │
  │                                                          │
  │  EPSG:3857  Web Mercator / Pseudo-Mercator               │
  │             Used by Google Maps tiles, OSM tiles         │
  │             Units: meters (but spherical approximation)  │
  │                                                          │
  │  EPSG:4269  NAD83 geographic (lat/lon, N. America)       │
  │             US federal standard                         │
  │                                                          │
  │  EPSG:32618  UTM Zone 18N (WGS84)                        │
  │  EPSG:326xx  UTM Zone xx N (WGS84) — xx = 01 to 60       │
  │  EPSG:327xx  UTM Zone xx S (WGS84)                       │
  │                                                          │
  │  EPSG:27700  British National Grid (OSGB36)              │
  │  EPSG:2154   French Lambert-93                           │
  │  EPSG:25832  ETRF89 / UTM Zone 32N (Germany/Netherlands) │
  └──────────────────────────────────────────────────────────┘

  CRS MISMATCH — THE #1 GIS ERROR:
  ┌──────────────────────────────────────────────────────────┐
  │  Data A: EPSG:4326 (degrees)                             │
  │  Data B: EPSG:3857 (meters)                              │
  │                                                          │
  │  Overlaying without reprojection: Africa appears where  │
  │  the North Sea should be. Classic beginner error.        │
  │                                                          │
  │  GIS tools: "project on the fly" (display only, risky)  │
  │             Transform/reproject (correct, permanent)     │
  └──────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

---

## Spatial Operations

The power of GIS is its spatial query and analysis operators. These are the SQL equivalents for spatial data.

```
SPATIAL OPERATIONS CATALOG
══════════════════════════════════════════════════════════════════════

  PROXIMITY:
  ├── Buffer: create polygon at distance d from feature
  │   Buffer(hospital, 5000m) → 5km service area polygon
  │
  ├── Nearest neighbor: find closest feature
  │   NearestNeighbor(parcels, hospitals) → nearest hospital per parcel
  │
  └── Distance: calculate distances between features

  OVERLAY:
  ├── Intersect: return features present in BOTH layers
  │   Intersect(parcels, flood_zone) → parcels in flood zone
  │
  ├── Union: combine all features from both layers
  │   Union(counties_A, counties_B) → merged layer
  │
  ├── Clip: cut one layer to the extent of another
  │   Clip(roads, study_area) → roads inside study area
  │
  └── Erase: remove features where they overlap another layer
      Erase(land, water_bodies) → land with lakes removed

  MEASUREMENT:
  ├── Area: polygon area calculation (using projection units)
  ├── Length: line length
  └── Perimeter: polygon perimeter

  SPATIAL JOINS:
  Join attributes from one layer to another based on spatial relationship
  SpatialJoin(parcels, census_tracts, "within") →
    each parcel gets its census tract's demographic attributes

  TOPOLOGICAL PREDICATES (DE-9IM model):
  ├── Equals: identical geometries
  ├── Disjoint: no shared points
  ├── Intersects: any shared point
  ├── Touches: share boundary, not interior
  ├── Crosses: interiors intersect (lines crossing)
  ├── Within: A entirely inside B
  ├── Contains: B entirely inside A
  └── Overlaps: interiors intersect, neither contains the other

  NETWORK ANALYSIS:
  ├── Shortest path: Dijkstra/A* on road network graph
  ├── Service area: all locations reachable within T minutes
  ├── Closest facility: nearest hospital/fire station/school
  └── Route optimization: TSP variants for delivery routing

══════════════════════════════════════════════════════════════════════
```

---

## Software Landscape

```
GIS SOFTWARE LANDSCAPE
══════════════════════════════════════════════════════════════════════

  ESRI / ArcGIS ECOSYSTEM (dominant commercial):
  ├── ArcGIS Pro: desktop GIS — the industry standard
  │   Government, utilities, transportation: ~90% market
  │   Steep learning curve, expensive license
  │   Python API + Jupyter integration (modern)
  ├── ArcGIS Online: cloud-hosted GIS + web maps
  ├── ArcGIS Enterprise: on-premises server GIS
  └── ArcPy: Python scripting interface

  OPEN SOURCE STACK:
  ├── QGIS: desktop GIS (ArcGIS alternative, free)
  │   Active community; covers most ArcGIS use cases
  │   Plugin ecosystem; Python scripting
  │
  ├── PostGIS: PostgreSQL extension (spatial SQL database)
  │   Spatial types: geometry, geography
  │   Spatial indexes: GiST, BRIN
  │   Full OGC Simple Features + many analysis functions
  │   The backend for most web GIS applications
  │
  ├── GDAL/OGR: foundational raster/vector library
  │   GDAL: raster (GeoTIFF, NetCDF, HDF, JPEG, PNG, etc.)
  │   OGR: vector (Shapefile, GeoJSON, KML, PostGIS, etc.)
  │   Powers: QGIS, PostGIS, Rasterio, Fiona, etc.
  │   CLI tools: gdal_translate, gdalwarp, ogr2ogr
  │
  ├── GeoServer / MapServer: WMS/WFS tile/feature servers
  │   Serve geodata as OGC web services
  │
  ├── Leaflet: JavaScript web mapping library (lightweight)
  │   Interactive maps in browser; tile-based; mobile-friendly
  │
  └── OpenLayers: JavaScript web mapping library (full-featured)
      WMS/WFS client support; rotation; advanced symbolization

  PYTHON ECOSYSTEM:
  ├── Shapely: geometry operations (GEOS bindings)
  ├── Fiona: vector I/O (OGR bindings)
  ├── Rasterio: raster I/O (GDAL bindings)
  ├── GeoPandas: spatial DataFrames (Shapely + Fiona + Pandas)
  ├── pyproj: coordinate transformations (PROJ bindings)
  ├── Folium: Leaflet maps from Python
  ├── Kepler.gl: high-performance WebGL mapping (Uber)
  └── Xarray + Rioxarray: raster cubes (time series rasters)

══════════════════════════════════════════════════════════════════════
```

The bridge to your background: PostGIS is PostgreSQL plus spatial types. If you know PostgreSQL, you know PostGIS except for the spatial predicates. The extension adds column types (geometry, geography), spatial indexes (GiST is an R-tree variant that organizes spatial data by bounding box hierarchies), and functions (ST_Distance, ST_Intersects, ST_Buffer, ST_Within, etc.).

```sql
-- PostGIS example: find all restaurants within 1km of a subway station
SELECT r.name, ST_Distance(r.geom, s.geom) AS dist_m
FROM restaurants r, subway_stations s
WHERE s.name = 'Times Square'
  AND ST_DWithin(r.geom, s.geom, 1000)
ORDER BY dist_m;
```

`ST_DWithin` uses the spatial index. `ST_Distance` computes the exact distance. This is SQL — the only unusual part is the spatial function names.

---

## Data Formats

```
GIS DATA FORMAT COMPARISON
══════════════════════════════════════════════════════════════════════

  VECTOR FORMATS:
  ┌───────────────┬──────────────────────────────────────────┐
  │  Shapefile    │ "Industry standard" — actually 3-4 files │
  │               │ .shp (geometry) + .dbf (attributes) +    │
  │               │ .prj (CRS) + .shx (spatial index)        │
  │               │ 2GB limit; field names ≤10 chars;        │
  │               │ no null values; one geometry type only   │
  │               │ Legacy but ubiquitous — still dominant   │
  │               │                                          │
  │  GeoJSON      │ JSON with geometry + properties          │
  │               │ Web-native; human-readable; text-based   │
  │               │ Good for small-medium web datasets       │
  │               │ No spatial index; slow for large data    │
  │               │                                          │
  │  GeoPackage   │ SQLite database with spatial extensions  │
  │               │ Single file (no multi-file mess)         │
  │               │ No size limit; multiple layers; tiles    │
  │               │ OGC standard; modern shapefile replace   │
  │               │                                          │
  │  KML/KMZ      │ Google Earth format; XML-based           │
  │               │ Good for visualization; poor for analysis│
  │               │                                          │
  │  FlatGeobuf   │ Binary, streamable, spatial index baked  │
  │               │ Fast for large datasets; web-optimized   │
  └───────────────┴──────────────────────────────────────────┘

  RASTER FORMATS:
  ┌───────────────┬──────────────────────────────────────────┐
  │  GeoTIFF      │ TIFF + embedded CRS (most common)        │
  │               │ Cloud-Optimized GeoTIFF (COG): partial   │
  │               │ reads over HTTP; the streaming standard  │
  │               │                                          │
  │  NetCDF/HDF5  │ Multi-dimensional arrays (climate data)  │
  │               │ Time as a dimension; good for data cubes │
  │               │                                          │
  │  JPEG2000     │ Compressed imagery; used by Planet, etc. │
  │               │                                          │
  │  MBTiles      │ SQLite-packed tiles (offline maps)       │
  └───────────────┴──────────────────────────────────────────┘

  THE SHAPEFILE PROBLEM:
  Shapefiles are a 1990s format (ESRI proprietary, then open spec).
  They are the GIS equivalent of the CSV: ubiquitous, limited, will
  never die. Use GeoPackage for new projects; support shapefile for
  data exchange with legacy users.

══════════════════════════════════════════════════════════════════════
```

---

## Web GIS Architecture

```
WEB GIS ARCHITECTURE
══════════════════════════════════════════════════════════════════════

  CLIENT (Browser):
  ┌──────────────────────────────────────────────────────────┐
  │  Leaflet / MapboxGL / OpenLayers (JavaScript)            │
  │  ├── Renders tiles (raster or vector)                   │
  │  ├── Renders GeoJSON features                           │
  │  ├── Handles pan/zoom/click interactions                │
  │  └── Makes WMS/WFS/tile requests                        │
  └──────────────────────────────────────────────────────────┘
         ↕ HTTP
  SERVER (Tile/Feature Server):
  ┌──────────────────────────────────────────────────────────┐
  │  GeoServer / MapServer / pg_tileserv / Martin            │
  │  ├── WMS: raster tile rendering (fixed style)           │
  │  ├── WFS: vector features + attributes (GeoJSON)        │
  │  ├── WMTS: pre-rendered raster tiles (cached)           │
  │  └── Vector Tiles (MVT): styled client-side             │
  └──────────────────────────────────────────────────────────┘
         ↕ SQL
  DATABASE:
  ┌──────────────────────────────────────────────────────────┐
  │  PostGIS (PostgreSQL + spatial extension)               │
  │  ├── Stores: geometries + attributes + spatial index    │
  │  ├── Answers: spatial queries in milliseconds           │
  │  └── CRS management, coordinate transformation (PROJ)   │
  └──────────────────────────────────────────────────────────┘

  TILE SCHEMES:
  Raster tiles: pre-rendered PNG at each z/x/y
  Vector tiles: Mapbox Vector Tiles (MVT/PBF binary)
    - Tiles contain feature geometries + attributes
    - Styling applied in browser (client-side)
    - One tile dataset, infinite styles
    - Much smaller than raster tiles + responsive

══════════════════════════════════════════════════════════════════════
```

---

## Bridge to Databases and Computing

GIS and relational databases converge at PostGIS. If you understand SQL, PostGIS is SQL plus spatial types. The conceptual mapping:

| Database concept | GIS equivalent |
|-----------------|---------------|
| Table | Layer / Feature class |
| Row | Feature |
| Column | Attribute field |
| PRIMARY KEY | Feature ID (FID/OID) |
| Geometry column | geometry type (Point, LineString, Polygon) |
| Spatial index (GiST) | R-tree on bounding boxes |
| ST_Intersects(a,b) | Spatial predicate (like JOIN ON + WHERE) |
| ST_Distance(a,b) | Spatial measure function |

The spatial index in PostGIS uses a GiST (Generalized Search Tree) implementation of an R-tree — which partitions space hierarchically by bounding box, allowing fast elimination of non-candidate geometries. The two-step spatial query: (1) filter by bounding box using index, (2) exact geometry test on candidates. This is the same two-stage filter that database range queries use.

---

## Common Confusion Points

**"GIS is just ArcGIS."** ArcGIS is the dominant commercial GIS platform. GIS is the discipline and the class of software. QGIS, PostGIS, and Python-based geospatial analysis are GIS but not ArcGIS.

**"I can just use Google Maps for GIS."** Google Maps is a consumer map viewer. It does not support data import, spatial queries, overlay analysis, custom styling, or batch processing. GIS is for analysis; Google Maps is for visualization.

**"Shapefile is fine."** For small projects, yes. The 2GB limit, 10-character field names, and multi-file format cause real problems at scale. Prefer GeoPackage or PostGIS for any serious work.

**"EPSG:4326 and EPSG:3857 are the same."** Both use WGS84 datum, but completely different projections. 4326 is geographic (degrees); 3857 is projected (meters) with significant area distortion. Using 4326 coordinates in a 3857 context or vice versa will produce wildly wrong results.

---

## Decision Cheat Sheet

| Task | Tool | Format |
|------|------|--------|
| Desktop analysis | QGIS or ArcGIS Pro | Any |
| Spatial SQL queries | PostGIS | PostGIS native |
| Web interactive map | Leaflet + GeoJSON or MVT | GeoJSON / MVT |
| Python spatial analysis | GeoPandas + Rasterio | GeoJSON / GeoTIFF |
| Data exchange (modern) | QGIS / ogr2ogr | GeoPackage |
| Data exchange (legacy) | QGIS / ogr2ogr | Shapefile |
| Raster analysis | GDAL CLI or Rasterio | GeoTIFF |
| Large-scale pipeline | PostGIS + Python | PostGIS tables |
| Format conversion | ogr2ogr / gdal_translate | Any → Any |
