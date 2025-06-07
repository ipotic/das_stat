# 01_calculate_building_weight.py

import pandas as pd
import numpy as np

# Define input and output paths
input_path = r"...\1_Input_Objects.csv"
output_path = r"...\01_calculate_building_weight.csv"

# Load input CSV file
df = pd.read_csv(input_path)

# Calculate the building weight as the product of area and number of floors
df["weight"] = df["area"] * df["floors"]

# Save the updated dataframe to CSV
df.to_csv(output_path, index=False)
