# 07_spearman_population_vs_distance.py

import pandas as pd
from scipy.stats import spearmanr

# Define input and output paths
input_path = r"...\06_ols_population_change.csv"
output_path = r"...\07_spearman_population_vs_distance.txt"

# Load input data (includes delta_pop and dist_center)
df = pd.read_csv(input_path)

# Spearman correlation
corr, pval = spearmanr(df["delta_pop"], df["dist_center"])

# Save result
with open(output_path, "w") as f:
    f.write("Spearman's rank correlation\n")
    f.write("----------------------------\n")
    f.write(f"Correlation coefficient (rho): {corr:.4f}\n")
    f.write(f"P-value: {pval:.4f}\n")
