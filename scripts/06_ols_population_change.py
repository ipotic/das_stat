# 06_ols_population_change.py

import pandas as pd
import geopandas as gpd
import statsmodels.api as sm
from shapely.geometry import Point

# Define paths
csv_path = r"...\04_calculate_population_dynamics.csv"
shp_path = r"...\shp\1_Input_Objects.shp"
output_txt = r"...\06_ols_population_change_summary.txt"
output_csv = r"...\06_ols_population_change.csv"

# Load population data
df = pd.read_csv(csv_path)

# Load building geometries
gdf = gpd.read_file(shp_path)[["ID", "geometry"]]
gdf = gdf.to_crs(epsg=32634)#caution using EPSG code, must be same as in SHP file

# Calculate centroid and settlement centre
gdf["centroid"] = gdf.centroid
settlement_center = Point(gdf["centroid"].x.mean(), gdf["centroid"].y.mean())

# Compute distance to settlement centre
gdf["dist_center"] = gdf["centroid"].distance(settlement_center)

# Merge with population data
df_final = pd.merge(df, gdf[["ID", "dist_center"]], on="ID")

# Save merged table with dist_center
df_final.to_csv(output_csv, index=False)

# OLS regression
y = df_final["delta_pop"]
X = df_final[["area", "floors", "dist_center"]]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

# Save OLS summary
with open(output_txt, "w") as f:
    f.write(model.summary().as_text())
