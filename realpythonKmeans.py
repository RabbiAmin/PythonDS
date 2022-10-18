# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:58:08 2022

@author: Rabbi Amin
"""

import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans


#n_samples is the total number of samples to generate.
#centers is the number of centers to generate.
#cluster_std is the standard deviation.
#make_blobs() returns a tuple of two values:

#1)A two-dimensional NumPy array with the x- and y-values for each of the samples
#@)A one-dimensional NumPy array containing the cluster labels for each sample

features, true_labels = make_blobs(
        n_samples=200,
        centers=3,
        cluster_std=2.75,
        random_state=42
   )


 # Instantiate k-means and dbscan algorithms
kmeans = KMeans(n_clusters=2)
dbscan = DBSCAN(eps=0.3)

# Fit the algorithms to the features
kmeans.fit(scaled_features)
dbscan.fit(scaled_features)

 # Compute the silhouette scores for each algorithm
kmeans_silhouette = silhouette_score(
    scaled_features, kmeans.labels_
).round(2)
dbscan_silhouette = silhouette_score(
    scaled_features, dbscan.labels_
).round (2)