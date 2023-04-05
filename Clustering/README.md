# Clustering 

Algorithm
1. Choose number of clusters, $k$
2. Randomly initilaise $k$ centroids
3. Calculate the (Euclidean) distance between each data point in the training set with the $k$ centroids
4. Assign each data point to the closest centroid
5. Update centroid location by taking the average of the points in each cluster group
6. Repeat steps 3, 4 and 5 until the centroids no longer change 


Numerical Procedure
1. Set up Python environment
2. Load and clean data
3. Define functions to initialise centroids, compute errors and run Kmeans algorithm
4. Run algorithm for various $k$ values to identify the number of clusters needed
5. Run algorithm for specified $k$ value
6. Visualise results
