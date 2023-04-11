'''
K-Means clustering algorithm from scratch
Dr. Robert Long

This script implements Kmeans clustering on an open-source dataset containing
retail transactions to achieve CUSTOMER SEGMENTATION.
The dataset can be found at 


The code is segmented into sections which isolate different processes, these
are summarised below and a brief desciption as to how much they each need to
be edited for different use cases.


Code structure:
    SECTION 1 - import modules
    SECTION 2 - load, clean and transform data
    SECTION 3 - define functions
    SECTION 4 - elbow method and visualise errors 
    SECTION 5 - implement Kmeans clustering algorithm and visualise clusters
    
    SECTION 1 - edit colour map and specify tasks to run (with parameters)
    SECTION 2 - this is the main section to be edited, very specific for each
        distinct data set
    SECTIONS 3 & 4 - these should not need much editing for general use cases
    SECTION 5 - the solver block should not need editing for general use 
        the visualisation block is problem specific
'''


#%%
''' 
SECTION 1 

Setup - import modules and define tasks to run
'''

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# define colour map for cluster plots
customcmap = ListedColormap(['darkturquoise','gold','seagreen','hotpink'])

print('SECTION 1')

# specify which tasks to run and values to use
run_elbow = True # Boolean to determine if elbow function should be run
centroid_trial = 3 # max. number of centroids for elbow survey

run_kmeans = True # Boolean to determine if clustering should be run
centroid_use = 4 # number of centroids to use for clustering

err_tol = 1E-4 #  error between iterations before considering as converged
make_plots = False # Boolean to determine if plots are generated
#%%
'''
SECTION 2

load, clean and transform data
'''

print('SECTION 2')

#%%
# Load, clean and aggregate data as necessary
# Problem specific code block

# read-in the excel spreadsheet using pandas 
df = pd.read_excel('Online_retail.xlsx', sheet_name='Online Retail')

# Remove  cancelled orders
df = df.loc[df['Quantity'] > 0]

# Remove any entries without CustomerID
df = df[pd.notnull(df['CustomerID'])]

# Remove incomplete month
df = df.loc[df['InvoiceDate'] < '2011-12-01']

# Calculate total sales from the Quantity and UnitPrice
df['Sales'] = df['Quantity'] * df['UnitPrice']

# use groupby to aggregate sales by CustomerID
customer_df = df.groupby('CustomerID').agg({'Sales': sum, 
                                            'InvoiceNo': lambda x: x.nunique()})

# Select the columns of interest
customer_df.columns = ['TotalSales', 'OrderCount'] 

# create a new column 'AvgOrderValue'
customer_df['AvgOrderValue'] = customer_df['TotalSales'] / customer_df['OrderCount']


rank_df = customer_df.rank(method='first')
# normalized_df = (rank_df - rank_df.mean()) / rank_df.std()
normalized_df =  2* (rank_df - rank_df.mean()) / (rank_df.max() - rank_df.min())
# normalized_df.head(10)

colnames = list(normalized_df.columns[1:-1])
working_df = normalized_df

#%%
'''
SECTION 3

Define functions to initiate clusters, calculate error and apply the kmeans clustering algorithm
'''

print('SECTION 3')
# Define functions used to initiate clusters, calculate error and
# apply the kmeans clustering algorithm

def initiate_centroids(k, dset):
    '''
    Select k data points as centroids
    k: number of centroids
    dset: pandas dataframe
    '''
    centroids = dset.sample(k)
    return centroids

def rsserr(a,b):
    '''
    Calculate the root of sum of squared errors. 
    a and b are numpy arrays
    '''
    return np.square(np.sum((a-b)**2)) 

def centroid_assignation(dset, centroids):
    '''
    Given a dataframe `dset` and a set of `centroids`, we assign each
    data point in `dset` to a centroid. 
    - dset - pandas dataframe with observations
    - centroids - pa das dataframe with centroids
    '''
    k = centroids.shape[0]
    n = dset.shape[0]
    assignation = []
    assign_errors = []

    for obs in range(n):
        # Estimate error
        all_errors = np.array([])
        for centroid in range(k):
            err = rsserr(centroids.iloc[centroid, :], dset.iloc[obs,:])
            all_errors = np.append(all_errors, err)

        # Get the nearest centroid and the error
        nearest_centroid =  np.where(all_errors==np.amin(all_errors))[0].tolist()[0]
        nearest_centroid_error = np.amin(all_errors)

        # Add values to corresponding lists
        assignation.append(nearest_centroid)
        assign_errors.append(nearest_centroid_error)

    return assignation, assign_errors

def kmeans(dset, k, err_tol):
    '''
    K-means implementation
    `dset`:  DataFrame with features
    `k`: number of clusters
    `tol`: numerical tolerance, default value of 1E-4
    '''
    # Let us work in a copy, so we don't mess the original
    working_dset = dset.copy()
    # We define some variables to hold the error, the 
    # stopping signal and a counter for the iterations
    err = []
    signal = True
    j = 0
    
    # Step 2: Initiate clusters by defining centroids 
    centroids = initiate_centroids(k, dset)

    while(signal):
        # Step 3 and 4 - Assign centroids and calculate error
        working_dset['centroid'], j_err = centroid_assignation(working_dset, centroids) 
        err.append(sum(j_err))
        
        # Step 5 - Update centroid position
        centroids = working_dset.groupby('centroid').agg('mean').reset_index(drop = True)
        # Step 6 - Restart the iteration
        if j>0:
            # Is the error less than a tolerance (1E-4)
            if err[j-1]-err[j]<=err_tol:
                signal = False
        j+=1
    print(j)
    working_dset['centroid'], j_err = centroid_assignation(working_dset, centroids)
    centroids = working_dset.groupby('centroid').agg('mean').reset_index(drop = True)
    return working_dset['centroid'], j_err, centroids

def elbow(dataset, n):
    '''
    Calculate total error for different numbers of clusters to work out how
    many are needed
    
    INPUT
    dataset: pandas dataframe containing cleaned data
    n: number of clusters to try/
    
    OUTPUT
    err_total: total Euclidean distance of all datapoints and closest centroid
    '''
    
    err_total = []
    dataset_elbow = dataset

    for i in range(n):
        print('Number of clusters - ', i+1)
        _, my_errs, _ = kmeans(dataset_elbow, i+1, err_tol)
        err_total.append(sum(my_errs))
    return err_total

#%%
''' 
SECTION 4 

Elbow method to work out optimal number of clusters 

Compute the total error increasing number of clusters - the optimal number is
determined by the number for which the curve begins to plateau
'''

print('SECTION 4')

if run_elbow == True:    
    totalerr = elbow(working_df, centroid_trial)
    
    if make_plots == True:
        # plot results
        fig, ax = plt.subplots(figsize=(8, 6), dpi=200)
        plt.plot(range(1,centroid_trial+1), totalerr, marker='o', color='purple')
        ax.set_xlabel(r'Number of clusters', fontsize=14)
        ax.set_ylabel(r'Total error', fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        plt.grid()
        plt.show()

#%%
'''
SECTION 5

Implement Kmeans clustering algorithm
'''

print('SECTION 5')

if run_kmeans == True:
    np.random.seed(10)
    
    df = working_df[['OrderCount','TotalSales','AvgOrderValue']]
    centroids = initiate_centroids(centroid_use, df)
    
    df['centroid'], df['error'] = centroid_assignation(df, centroids)
    
    customcmap = ListedColormap(['darkturquoise','gold','seagreen','hotpink'])
    if make_plots == True:
        plt.scatter(df.iloc[:,0], df.iloc[:,1],  c=df['centroid'].iloc[:], cmap=customcmap, edgecolor='k')
    print("The total error is {0:.2f}".format(df['error'].sum()))
    centroids = df.groupby('centroid').agg('mean').loc[:, colnames].reset_index(drop = True)    
    np.random.seed(42)
    df['centroid'], df['error'], centroids =  kmeans(df[['OrderCount','TotalSales', 'AvgOrderValue']], centroid_use, err_tol)

    #%%
    if make_plots == True:
        plt.figure(figsize=(10,3), dpi=300)
        plt.subplot(1,3,1)
        plt.xlabel('Order Count'); plt.ylabel('Total Sales')
        plt.scatter(df.iloc[:,0], df.iloc[:,1],  c=df['centroid'].iloc[:], cmap=customcmap, edgecolor='k')
        plt.scatter(centroids.iloc[:,0], centroids.iloc[:,1], marker = 's', color='k', edgecolor='w')
        plt.subplot(1,3,2)
        plt.xlabel('Order Count'); plt.ylabel('Average Order Value')
        plt.scatter(df.iloc[:,0], df.iloc[:,2],  c=df['centroid'].iloc[:], cmap=customcmap, edgecolor='k')
        plt.scatter(centroids.iloc[:,0], centroids.iloc[:,2], marker = 's', color='k', edgecolor='w')
        plt.subplot(1,3,3)
        plt.scatter(df.iloc[:,1], df.iloc[:,2],  c=df['centroid'].iloc[:], cmap=customcmap, edgecolor='k')
        plt.scatter(centroids.iloc[:,1], centroids.iloc[:,2], marker = 's', color='k', edgecolor='w') 
        plt.grid()
        plt.tight_layout()
        plt.show()

        # optional code to write the positions of the final centroids to a 
        # txt file. 
        # this can be useful if runs take a while to complete and you want to
        # edit a figure iteratively without regenerating the data
        # path = r'./final_clusters.txt'
        # 
        #with open(path, 'a') as f:
        #    df_string = df.to_string(header=True, index = False)
        #    f.write(df_string)
        # df.to_csv('raw_data.csv', index=False)
        # df.to_excel('raw_data.xls', index=False)
#%%
# Attempting to track centroids as multiple iterations of the clustering 
# algorithm are performed. 

# Should probably tabulate the number of iterations needed to converge for 
# each k value checked in making the elbow plot

