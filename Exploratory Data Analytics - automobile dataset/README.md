# Exploratory Data Analysis (EDA) on Automobiles Dataset

This repository contains a Jupyter Notebook performing Exploratory Data Analysis on the Automobiles dataset. The analysis focuses on cleaning the data, handling missing values, and generating insights through visualizations on aspects like fuel efficiency, price comparisons, engine capacity, and manufacturer model counts. A PDF report summarizes the key findings with embedded visualizations.

The dataset explores various automobile attributes such as make, model, fuel type, MPG, price, and more, to uncover patterns in sales, efficiency, and performance.

---

## Repository Structure

```
- automobiles.ipynb          # Jupyter Notebook with EDA code
- automobile.txt             # Raw dataset (CSV format)
- EDA Report - Automobile Dataset.pdf  # Summary report with insights and visualizations
- README.md                  # This file
```


## Key Sections in the Notebook

1. **Data Loading and Inspection**: Load the dataset, display initial rows, info, and check for missing values.
2. **Data Cleaning**: Remove redundant columns (`normalized-losses`, `symboling`), drop duplicates, convert data types, handle missing values by replacing '?' with NaN and dropping them.
3. **Exploratory Analysis and Visualizations**:
   - Count of hatchback automobiles.
   - Comparison of most expensive vs. cheapest cars (price, city MPG, highway MPG) using bar plots.
   - Average fuel efficiency (MPG) by manufacturer, with bar plots for combined, city, and highway MPG.
   - Vehicles with the largest engine capacity, sorted by engine size.
   - Manufacturer with the most car models, using value counts.
4. **Insights**: Derived from visualizations, such as fuel-efficient brands (e.g., Honda, Toyota) vs. performance-oriented ones (e.g., Jaguar, Porsche).

## Dataset Overview

- **Source**: `automobile.txt` (comma-separated values).
- **Rows**: 205 (vehicles).
- **Columns**: 26 (e.g., make, fuel-type, body-style, engine-size, price, city-mpg, highway-mpg).
- **Data Types**: Mix of integers, floats, and objects.
- **Missing Values**: Handled by replacing '?' with NaN and dropping rows.

Sample data (first few rows):
```
symboling,normalized-losses,make,fuel-type,aspiration,num-of-doors,body-style,drive-wheels,engine-location,wheel-base,length,width,height,curb-weight,engine-type,num-of-cylinders,engine-size,fuel-system,bore,stroke,compression-ratio,horsepower,peak-rpm,city-mpg,highway-mpg,price
3,?,alfa-romero,gas,std,two,convertible,rwd,front,88.60,168.80,64.10,48.80,2548,dohc,four,130,mpfi,3.47,2.68,9.00,111,5000,21,27,13495
...
```

## Requirements

- Python 3.x
- Libraries (install via `pip install -r requirements.txt` if provided, or manually):
  - `numpy`
  - `pandas`
  - `seaborn`
  - `matplotlib`

## How to Run

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```
   pip install numpy pandas seaborn matplotlib
   ```

3. Open the Jupyter Notebook:
   ```
   jupyter notebook automobiles.ipynb
   ```

4. Run cell by cell to perform the EDA and generate visualizations.

5. View the PDF report (`EDA Report - Automobile Dataset.pdf`) for a summarized version with insights.

## Insights from the Report

- **Hatchbacks**: There are 70 hatchback automobiles in the dataset.
- **Price & MPG Comparison**: Most expensive cars (e.g., Mercedes-Benz at ~$45,000) have lower MPG (~16-19), while cheapest (e.g., Chevrolet at ~$5,000) offer higher MPG (~38-47).
- **Fuel Efficiency**: Honda and Subaru lead in average MPG; luxury brands like Jaguar lag behind.
- **Engine Capacity**: Largest engines in Jaguar (326 cc) and Mercedes-Benz (308 cc) models.
- **Most Models**: Toyota has the most models (32), followed by Nissan (18).

For detailed observations and trends, refer to the PDF report.

## Author

This EDA and report were prepared by **Koketso Llale**.

Feel free to contribute or raise issues for improvements!
