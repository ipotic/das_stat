# 03_allocate_population_counts.py

import pandas as pd
import numpy as np

# Define input and output paths
input_path = r"...\02_allocate_population_share.csv"
output_path = r"...\03_allocate_population_counts.csv"

# Load input CSV file with weight shares
df = pd.read_csv(input_path)

# Allocate 2011 and 2022 population proportionally to each building
df["p11_alloc"] = df["pop2011"] * df["weight_share"]
df["p22_alloc"] = df["pop2022"] * df["weight_share"]

# Save the updated dataframe to CSV
df.to_csv(output_path, index=False)
