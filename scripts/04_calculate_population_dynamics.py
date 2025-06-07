# 04_calculate_population_dynamics.py

import pandas as pd
import numpy as np

# Define input and output paths
input_path = r"...\03_allocate_population_counts.csv"
output_path = r"...\04_calculate_population_dynamics.csv"

# Load input CSV file with allocated population
df = pd.read_csv(input_path)

# A) Absolute population change
df["delta_pop"] = df["p22_alloc"] - df["p11_alloc"]

# B) Relative population change (%) with division-by-zero handling
df["delta_pct"] = np.where(
    df["p11_alloc"] > 0,
    (df["delta_pop"] / df["p11_alloc"]) * 100,
    np.nan  # or 0 if you prefer
)

# C) Population density for 2011 and 2022
df["dens11"] = df["p11_alloc"] / df["area"]
df["dens22"] = df["p22_alloc"] / df["area"]

# Change in density
df["delta_dens"] = df["dens22"] - df["dens11"]

# Save the updated dataframe to CSV
df.to_csv(output_path, index=False)
