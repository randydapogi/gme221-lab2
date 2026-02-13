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

### Process Reflection Milestone

1. Why CRS transformation is necessary before area computation?

- The parcel and landuse data we loaded from the PostGIS was in 4326 projection based on the print statement we performed. The EPSG:4326 projection is in degrees. To calculate the area of the geometry in meters we need to transform the projection from degrees to meters that is why we reprojected the parcel and landuse data to EPSG:3395 since this projection is in meters.

2. How does CRS choice affect area accuracy?

- Since CRS accuracy is optimized to be accurate to a certain region of the earth surface, CRS choice can affect the area accuracy calculation with accuracy dependent on the distance of the geometry in question to the optimized region of the CRS of choice.

3. Does the overlay create new spatial units that did not previously exist?

- In our analysis.py script, the overlay operatation created new geometry that are the intersections between the parcels and landuse.

4. Why classification is considered part of the analysis process?

- Classification is part of the analysis process because it performs an operation that transforms the output of the analysis process.

5. Is classification sensitive to sliver geometries or topology errors?

- In our example, classification is not sensitive to sliver geometries and topology errors since it performs its classification operation on each row of the input data independent of the geometry of the other rows in the input data.

6. Would changing the dominance threshold alter spatial patterns?

- Yes. Changing the dominance threshold alter the spatial pattern of the result from performing classification to the overlay input. Changing the dominance threshold will change the number of rows in the overlay dataframe that will be filtered in the classification operation. This will in turn change the overall geometry of the output of the classification.

### Challenge Exercise

1. What spatial question did you choose?

- I choose Option 3 — Small but Dense Residential Fragments.

2. What algorithmic steps did you design?

- For the challenge I performed the following steps
  - Load parcel and landuse data into GeoDataFrames
  - Reproject data to EPSG:3395 for area calculations
  - Calculate parcel area
  - Perform intersection overlay between parcel and landuse
  - Calculate landuse area and percentage of the overlay result
  - Perform classification by filtering the name property to residential, percentage property to less than 30 and total_area property to greater than 500
  - Transform data back to 4326
  - Save the geojson file

3. How does your logic differ from the guided example?

- The logic of my challenge script has a different filter parameters when filtering the overlay dataframe for data that satisfied the conditions of the challenge option. The other steps are the same as the guided example.
