# GmE 221 – Laboratory Exercise 2

## Overview

This laboratory performs a parcel–landuse overlay analysis using Python (GeoPandas).
Spatial data are retrieved from PostGIS using minimal SQL.
Overlay, area computation, percentage calculation, and classification are executed in Python.
The final output is exported as a GeoJSON file for visualization in QGIS.

---

## Environment Setup

- Python 3.x
- PostgreSQL with PostGIS
- GeoPandas, SQLAlchemy, psycopg2

## How to Run

1. Activate the virtual environment
2. Run `analysis.py` to execute the overlay and classification
3. Load the generated GeoJSON file in QGIS

---

## Outputs

- GeoJSON file: `output/dominant_residential.geojson`
- Visualization in QGIS

---

## Reflection

### Interpreting GIS IO in Practice

1. What is the difference between storing geometry in PostGIS and representing it in GeoPandas?

- The geometry stored in PostGIS and represented in GeoPandas are effectively the same geometry. However for our usecase we use PostGIS for the storage of our geometry data for the use of our different application. We then use GeoPandas to represent the geometry from the PostGIS database. Representing the geometry from PostGIS to GeoPandas lets us perform computations and transformations to the geometry without modifiying the original geometry stored in the PostGIS.

2. Why is this step considered Input (IO) rather than analysis?

- This is considered Input (IO) because we are just loading the data from PostGIS to GeoPandas without performing operations or modifying the data from the PostGIS.

3. How does this relate to the “Input / Process / Output” structure of GIS algorithms discussed in Lecture 3?

- In this case, we treat the PostGIS data as the input of our GIS algorithm. We treat the python script that reads the PostGIS data and performs calculations and analysis as the Process of the GIS algorithm and we treat the output generated from the python script as the output.
