# 02_allocate_population_share.py

import pandas as pd
import numpy as np

# Define input and output paths
input_path = r"...\01_calculate_building_weight.csv"
output_path = r"...\02_allocate_population_share.csv"

# Load input CSV file with calculated weights
df = pd.read_csv(input_path)

# Calculate the total weight across all residential buildings
total_weight = df["weight"].sum()

# Calculate each building's weight share relative to the total weight
df["weight_share"] = df["weight"] / total_weight

# Save the updated dataframe to CSV
df.to_csv(output_path, index=False)
