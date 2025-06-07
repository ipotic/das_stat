# 05_global_morans_I.py

import pandas as pd
import numpy as np
import geopandas as gpd
from libpysal.weights import KNN
from esda.moran import Moran

# Define input paths
input_csv = r"...\04_calculate_population_dynamics.csv"
input_shp = r"...\shp\1_Input_Objects.shp"
output_txt = r"...\05_global_morans_I_results.txt"

# Load CSV with population indicators
df = pd.read_csv(input_csv)

# Load shapefile with geometry
gdf_geom = gpd.read_file(input_shp)[["ID", "geometry"]]

# Merge CSV data with spatial geometry using 'ID'
gdf = gdf_geom.merge(df, on="ID")

# Ensure projected CRS (EPSG:32634 is confirmed)
if not gdf.crs or gdf.crs.to_epsg() != 32634:#caution using EPSG code, must be same as in SHP file
    gdf = gdf.to_crs(epsg=32634)#caution using EPSG code, must be same as in SHP file

# Create spatial weights matrix using 8 nearest neighbors
w = KNN.from_dataframe(gdf, k=8)
w.transform = 'r'

# Calculate Global Moran's I for delta_pop
moran_pop = Moran(gdf["delta_pop"], w)

# Calculate Global Moran's I for delta_dens
moran_dens = Moran(gdf["delta_dens"], w)

# Write results to text file
with open(output_txt, "w") as f:
    f.write("Global Moran's I results\n")
    f.write("------------------------\n")
    f.write(f"delta_pop:\n  I = {moran_pop.I:.4f}, p = {moran_pop.p_sim:.4f}, z = {moran_pop.z_sim:.2f}\n\n")
    f.write(f"delta_dens:\n  I = {moran_dens.I:.4f}, p = {moran_dens.p_sim:.4f}, z = {moran_dens.z_sim:.2f}\n")
