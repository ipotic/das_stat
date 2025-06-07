import os
import pandas as pd
import geopandas as gpd
from libpysal.weights import KNN
from esda.getisord import G_Local

# Input and output paths
input_csv = r"...\04_calculate_population_dynamics.csv"
input_shp = r"...\shp\1_Input_Objects.shp"
output_csv = r"...\08_getis_ord_gi_star.csv"
output_shp_folder = r"...\08_getis_ord_gi_star_shp"
output_shp_path = os.path.join(output_shp_folder, "08_getis_ord_gi_star.shp")

os.makedirs(output_shp_folder, exist_ok=True)

# read data
df = pd.read_csv(input_csv)
gdf = gpd.read_file(input_shp)[["ID", "geometry"]]
gdf = gdf.to_crs(epsg=32634)

# tables merge
gdf = gdf.merge(df[["ID", "delta_dens"]], on="ID")

# knn weights (kNN)
w = KNN.from_dataframe(gdf, k=8)
w.transform = 'r'

# Getis-Ord Gi*
gi_star = G_Local(gdf["delta_dens"], w)

# Z-score i p-values (-style column Labels)
gdf["GiZScore_IDW_100"] = gi_star.Zs
gdf["GiPValue_IDW_100"] = gi_star.p_sim

# classification (desired logic)
def classify_gi_bin(z, p):
    if z <= -2.58 and p <= 0.01:
        return -3  # Cold Spot 99%
    elif z <= -1.96 and p <= 0.05:
        return -2  # Cold Spot 95%
    elif z <= -1.65 and p <= 0.10:
        return -1  # Cold Spot 90%
    elif z >= 2.58 and p <= 0.01:
        return 3   # Hot Spot 99%
    elif z >= 1.96 and p <= 0.05:
        return 2   # Hot Spot 95%
    elif z >= 1.65 and p <= 0.10:
        return 1   # Hot Spot 90%
    else:
        return 0   # Not significant

gdf["Gi_Bin_IDW_100"] = [classify_gi_bin(z, p) for z, p in zip(gdf["GiZScore_IDW_100"], gdf["GiPValue_IDW_100"])]

# save results
gdf.to_file(output_shp_path)
gdf.drop(columns="geometry").to_csv(output_csv, index=False)
