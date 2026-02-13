import geopandas as gpd 
from sqlalchemy import create_engine

# Database connection parameters 
host = "localhost" 
port = "5432" 
dbname = "gme221" 
user = "postgres" 
password = "admin" 

# Create the connection string 
conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}" 

# Create the database engine 
engine = create_engine(conn_str) 


# Minimal SQL queries (no spatial operations) 
sql_parcel = "SELECT parcel_pin, geom FROM public.parcel" 
sql_landuse = "SELECT name, geom FROM public.landuse" 

# Load data into GeoDataFrames 
parcels = gpd.read_postgis(sql_parcel, engine, geom_col="geom") 
landuse = gpd.read_postgis(sql_landuse, engine, geom_col="geom") 


# Reproject to EPSG:3395 for area calculations 
parcels = parcels.to_crs(epsg=3395) 
landuse = landuse.to_crs(epsg=3395)

# Calculate parcel area
parcels["total_area"] = parcels.geometry.area 

# Perform intersection overlay between parcel and landuse
overlay = gpd.overlay(parcels, landuse, how="intersection") 
overlay["landuse_area"] = overlay.geometry.area 

# calculate area percentage
overlay["percentage"] = ( overlay["landuse_area"] / overlay["total_area"] ) * 100 
overlay["percentage"] = overlay["percentage"].round(2) 


# Option 3 — Small but Dense Residential Fragments
#   - Identify residential fragments that:
#   - occupy less than 30% of the parcel
#   - but exceed a minimum area threshold (e.g., 500 m²)

# Perform classification
small_res = overlay[ 
                # Identify residential fragments that
                ((overlay["name"] == "Residential Zone - Low Density") | (overlay["name"] == "Residential Zone - Medium Density")) 
                # occupy less than 30% of the parcel
                & (overlay["percentage"] < 30) 
                # but exceed a minimum area threshold (e.g., 500 m²)
                & (overlay["total_area"] > 500) 
            ].copy() 

# transform data back to 4326
small_res = small_res.to_crs(epsg=4326)

# save geojson file
small_res.to_file( "output/challenge_result.geojson", driver="GeoJSON" ) 
print("GeoJSON saved successfully.")