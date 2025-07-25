# Building-Level Dasymetric Mapping of Population Change in a Depopulating Rural Settlement: A Case Study from Southeastern Serbia

This repository contains data, Python scripts, and visual outputs related to the study of building-level population change in a rural settlement in Southeastern Serbia. The project applies dasymetric mapping techniques, spatial statistics, and exploratory spatial data analysis to examine patterns of residential depopulation and intensification. The analysis combines spatial data processing in QGIS with Python scripting to identify statistically significant clusters of population density change at the building level.

## Structure

das_stat/

├── data/

│   ├── raw/

│   │   ├── shp/

│   │   └── csv/

│   └── processed/

├── notebooks/

├── scripts/

├── outputs/

│   ├── figures/

│   └── tables/

├── LICENSE

├── README.md

└── .gitignore

## Dependencies
The following Python libraries are used throughout the project:

pandas

numpy

geopandas

matplotlib

scipy

shapely

statsmodels

pysal

esda

To install all dependencies at once:

pip install pandas numpy geopandas matplotlib scipy shapely statsmodels pysal esda

## Data
data/raw/shp/: Original shapefiles used as input for the spatial analysis.

data/raw/csv/: CSV files containing outputs from the Gi* analysis.

data/processed/: Cleaned and prepared datasets used for statistical modelling and plotting.

## Outputs
outputs/figures/: Visualisations of analytical results.

outputs/tables/: Statistical tables including descriptive statistics and test results.

## License
The source code in this repository is licensed under the MIT License.
Tabular datasets and visual outputs are released under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

## Citation
Author. (YYYY). *Building-Level Dasymetric Mapping of Population Change in a Depopulating Rural Settlement: A Case Study from Southeastern Serbia* [Unpublished manuscript].

# das_stat
Dasymetric and statistics
