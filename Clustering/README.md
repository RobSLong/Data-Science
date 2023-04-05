# Clustering 
This repository contains 2 projects focused on Clustering machine learning - one focusing on the fundamentals of the Kmeans clustering algorithm and applies this to a retail data set, the other attempts to classify types of exoplanets. Both projects use open-source data sets and are intended to be a self-contained project with adequate enough documentation to be used as educational content.

Each directory herein contains a self-contained project with the naming convention <method-application> e.g. Clustering-retail is a project which applies clustering machine learning to a retail data set. The <README>.md in each directory should provide enough information to understand the problem and provide a foundation for similar projects to be undertaken!

  
  
Algorithm
1. Choose number of clusters, $k$
2. Randomly initilaise $k$ centroids
3. Calculate the (Euclidean) distance between each data point in the training set with the $k$ centroids
4. Assign each data point to the closest centroid
5. Update centroid location by taking the average of the points in eac0h cluster group
6. Repeat steps 3, 4 and 5 until the centroids no longer change 


Numerical Procedure
1. Set up Python environment
2. Load and clean data
3. Define functions to initialise centroids, compute errors and run Kmeans algorithm
4. Run algorithm for various $k$ values to identify the number of clusters needed
5. Run algorithm for specified $k$ value
6. Visualise results

Project Highlights
Customer segmentation
This project outlines the theory and numerical implementation of Kmeans clustering to an open-source retail data set. We show an implementation from scratch and one using sci-kit learn module. We present an end-to-end project, from loading and cleaning the data, applying the algorithm, visualising results and drawing conclusions from the model.
  
Types of Exoplanet
This project uses an open-source dataset of observed exoplanets and we use sci-kit learn to identify different types of exoplanet based on their mass and ____. We show that previously identified types of exoplanet predicted by theory are bore out in our machine learning framework.

