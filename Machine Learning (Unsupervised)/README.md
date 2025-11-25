# Principal Component Analysis and Clustering on US Arrests Dataset

## Project Overview

This project performs Principal Component Analysis (PCA) and clustering techniques on the US Arrests dataset to explore the patterns of crime rates and urban populations across different states in the United States. The goal is to reduce the dimensionality of the data while retaining important information and then group states with similar characteristics using K-Means and Hierarchical clustering.

## Dataset

The dataset used in this analysis is the `USArrests.csv` dataset, which contains statistics for 50 US states, namely:

*   `Murder`: Murder arrests per 100,000 population
*   `Assault`: Assault arrests per 100,000 population
*   `UrbanPop`: Percent urban population
*   `Rape`: Rape arrests per 100,000 population

## Analysis Steps

1.  **Data Loading and Exploration**: The dataset was loaded and initially explored to understand its structure, check for missing values, and view descriptive statistics.
2.  **Correlation Analysis**: A correlation matrix and heatmap were generated to visualize the relationships between the numerical variables.
3.  **Data Scaling**: The numerical features were scaled using `StandardScaler` to ensure each feature contributes equally to the PCA.
4.  **Principal Component Analysis (PCA)**: PCA was performed on the scaled data to reduce dimensionality. The first two principal components were extracted for visualization and clustering.
5.  **Biplot Visualization and Interpretation**: A biplot of the first two principal components was created to visualize the states and the influence of the original variables on these components. The biplot was interpreted to understand the main sources of variance in the data.
6.  **Determining the Optimal Number of Clusters**: The elbow method and silhouette scores were used to help determine an appropriate number of clusters for the dataset.
7.  **K-Means Clustering**: The K-Means algorithm was applied to the principal components using the chosen number of clusters.
8.  **Hierarchical Clustering**: Agglomerative Hierarchical clustering was applied to the principal components using the same number of clusters.
9.  **Cluster Analysis**: The characteristics of the states within each cluster for both K-Means and Hierarchical clustering were analyzed by examining the mean values of the original variables within each cluster.
10. **Comparison of Clustering Results**: The cluster assignments and characteristics from K-Means and Hierarchical clustering were compared to assess the similarities and differences in the groupings identified by the two methods.

## Key Findings

*   The correlation analysis revealed strong positive correlations between the violent crime rates (Murder, Assault, and Rape), while Urban Population had weaker correlations with these crimes.
*   The first two principal components explained a significant portion of the variance in the data (approximately 87%), with PC1 primarily capturing the overall level of violent crime and PC2 related to urban population.
*   Based on the elbow method and silhouette scores, 3 clusters were determined to be appropriate for the dataset.
*   Both K-Means and Hierarchical clustering methods identified three clusters with very similar characteristics, primarily differentiating states based on their overall level of violent crime and, to a lesser extent, their urban population.
*   States within the same cluster in both methods share similar profiles in terms of their original crime statistics and are located in close proximity to each other in the PCA-reduced space. One cluster represents states with low crime/low urban population, another with high crime/moderate urban population, and a third with moderate crime/high urban population.

## Conclusion

The analysis successfully applied PCA to reduce the dimensionality of the US Arrests dataset and utilized K-Means and Hierarchical clustering to identify meaningful groupings of states based on their crime rates and urban populations. The consistent results from both clustering methods indicate a robust underlying structure in the data, providing valuable insights into the patterns of crime and urbanization across the US states.
