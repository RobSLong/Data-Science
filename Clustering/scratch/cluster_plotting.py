'''
Generate figures using the clustering algorithm
Dr. Robert Long

This script generates two plots
- a plot of the data showing the final clusters
- a plot of the error vs the number of centroids used (ELBOW plot)

'''

import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# define colour map for cluster plots
customcmap = ListedColormap(['darkturquoise','gold','seagreen','hotpink'])


# Read data
clusters = pd.read_csv(r'raw_data.csv')
elbow = pd.read_csv(r'elbow.csv')


#%%
# Generate plot showing clustering in different parameter spaces

# Define plotting function to make each of the subplots
def plot_func(ind_plot, xstring, ystring, ind_x, ind_y):
    '''
    Generate a subplot
    ind_plot: index specifying which subplot to access
    xstring: label for x-axis (string)
    ystring: label for y-axis (string)
    ind_x: index specifying dataframe column plotted on x-axis
    ind_y: index specifying dataframe column plotted on y-axis
    '''
    plt.subplot(1,3,ind_plot)
    plt.xlabel(xstring); plt.ylabel(ystring)
    plt.scatter(clusters.iloc[:,ind_x], clusters.iloc[:,ind_y],  c=clusters['centroid'].iloc[:], cmap=customcmap, edgecolor='k')
    plt.grid(alpha=0.5)


# Generate and save plot
plt.figure(figsize=(10,3), dpi=300)
plot_func(1, 'Order count', 'Total sales', 0, 1)
plot_func(2, 'Order count', 'Average order values', 0, 2)
plot_func(3, 'Total sales', 'Average order values', 1, 2)
plt.tight_layout()
plt.savefig('cluster_customer_segmentation.png')
plt.show()

#%%
# Generate figure showing the error vs number of centroids
# aka Elbow plot

plt.figure(figsize=(3.4,3), dpi=300)
plt.plot(elbow.iloc[:,0], elbow.iloc[:,1], 'ko-')
plt.grid(alpha=0.5)
plt.xlabel('Number of centroids'); plt.ylabel('Error')
plt.tight_layout()
plt.savefig('elbow_customer_segmentation.png')
plt.show()
