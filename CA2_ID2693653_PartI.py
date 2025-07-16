# Burak Ayaeriş 2693653

from math import inf
import time as t
import pandas as pd
import numpy as np
from kmeans_ID2693653 import *
from init_centers_ID2693653 import *
from bisecting_k_means_ID2693653 import *
import matplotlib.pyplot as plt

# For K-means
begin = t.time()
derma_df = pd.read_excel("dermatology.xlsx",header=None)

# standardizing the data
derma_df = (derma_df - derma_df.mean()) / derma_df.std()

derma_np = derma_df.to_numpy()

# number of clusters
k = 10
 
a_best_value_sse = inf


for i in range(200):
    nearest_center_indices_array, sse_values_array, total_sse_value, num_iterations = k_means(derma_np, k)
    if total_sse_value < a_best_value_sse:
        a_best_value_sse = total_sse_value
        a_best_clustering_sizes = []
        for cluster in range(k):
            a_best_clustering_sizes.append(int(np.sum(nearest_center_indices_array == cluster)))
        iters = num_iterations
end = t.time()

a_time_elapsed = end - begin
print("\n")
print("K-means clustering results:")
print(f"Best SSE value: {a_best_value_sse:.2f}")
print(f"Best clustering sizes: {a_best_clustering_sizes}")
print(f"Time elapsed: {a_time_elapsed:.2f} seconds")
print(f"SSE list: {sse_values_array}")
print(f"Number of iterations: {iters}")


# For Bisecting K-means (50 initializations)
begin = t.time()
derma_df = pd.read_excel("dermatology.xlsx",header=None)

# standardizing the data
derma_df = (derma_df - derma_df.mean()) / derma_df.std()

derma_np = derma_df.to_numpy()

# number of clusters
k = 10 


bisecting_clustering_sizes = np.zeros(k, dtype=int)
nearest_center_indices_array_bk_50, sse_values_array, total_sse_value = bisecting_k_means(derma_np, k, 50)

for b_cluster in range(k):
    bisecting_clustering_sizes[b_cluster] = int(np.sum(nearest_center_indices_array_bk_50 == b_cluster))


end = t.time()
b_time_elapsed = end - begin
print("\n")
print("Bisecting K-means with 50 initializations:")
print(f"Best SSE value: {total_sse_value:.2f}")
print(f"Time elapsed: {b_time_elapsed:.2f} seconds")
print(f"Clustering sizes: {bisecting_clustering_sizes}")
print(f"SSE list: {sse_values_array}")

# For Bisecting K-means (100 initializations)

begin = t.time()
derma_df = pd.read_excel("dermatology.xlsx",header=None)

# standardizing the data
derma_df = (derma_df - derma_df.mean()) / derma_df.std()

derma_np = derma_df.to_numpy()

# number of clusters
k = 10 


bisecting_clustering_sizes = np.zeros(k, dtype=int)
nearest_center_indices_array_bk_100, sse_values_array, total_sse_value = bisecting_k_means(derma_np, k, 100)

for b_cluster in range(k):
    bisecting_clustering_sizes[b_cluster] = int(np.sum(nearest_center_indices_array_bk_100 == b_cluster))


end = t.time()
b_time_elapsed = end - begin
print("\n")
print("Bisecting K-means with 100 initializations:")
print(f"Best SSE value: {total_sse_value:.2f}")
print(f"Time elapsed: {b_time_elapsed:.2f} seconds")
print(f"Clustering sizes: {bisecting_clustering_sizes}")
print(f"SSE list: {sse_values_array}")


# Part c and d

k_values = range(3, 11)
kmeans_results = {"k": [], "SSE": [], "Time": [], "Cluster Sizes": []}
bisecting_results = {"k": [], "SSE": [], "Time": [], "Cluster Sizes": []}


for k in k_values:
    # K-means
    begin = t.time()
    a_best_value_sse = inf
    best_cluster_sizes = []
    for i in range(200): # 200 initializations
        nearest_center_indices_array, sse_values_array, total_sse_value, num_iterations = k_means(derma_np, k)
        if total_sse_value < a_best_value_sse:
            a_best_value_sse = total_sse_value
            best_cluster_sizes = [int(np.sum(nearest_center_indices_array == cluster)) for cluster in range(k)]
    end = t.time()
    kmeans_results["k"].append(k)
    kmeans_results["SSE"].append(a_best_value_sse)
    kmeans_results["Time"].append(end - begin)
    kmeans_results["Cluster Sizes"].append(best_cluster_sizes)

    # Bisecting K-means (for comparison, changing between 50 and 100 initializations)
    begin = t.time()
    nearest_center_indices_array_bk, sse_values_array, total_sse_value = bisecting_k_means(derma_np, k, 100) # num_initializations = 100 or 50
    cluster_sizes = [int(np.sum(nearest_center_indices_array_bk == cluster)) for cluster in range(k)]
    end = t.time()
    bisecting_results["k"].append(k)
    bisecting_results["SSE"].append(total_sse_value)
    bisecting_results["Time"].append(end - begin)
    bisecting_results["Cluster Sizes"].append(cluster_sizes)



print("\nComparison of K-means and Bisecting K-means:")
print(f"{'k':<5}{'K-means SSE':<15}{'K-means Time':<15}{'Bisecting SSE':<15}{'Bisecting Time':<15}")
for i in range(len(k_values)):
    print(f"{kmeans_results['k'][i]:<5}{kmeans_results['SSE'][i]:<15.2f}{kmeans_results['Time'][i]:<15.2f}"
          f"{bisecting_results['SSE'][i]:<15.2f}{bisecting_results['Time'][i]:<15.2f}")
    print(f"  K-means Cluster Sizes: {kmeans_results['Cluster Sizes'][i]}")
    print(f"  Bisecting Cluster Sizes: {bisecting_results['Cluster Sizes'][i]}")


plt.figure(figsize=(10, 5))
plt.plot(kmeans_results["k"], kmeans_results["SSE"], label="K-means SSE", marker='o')
plt.plot(bisecting_results["k"], bisecting_results["SSE"], label="Bisecting K-means SSE", marker='o')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("SSE")
plt.title("SSE vs Number of Clusters")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(kmeans_results["k"], kmeans_results["Time"], label="K-means Time", marker='o')
plt.plot(bisecting_results["k"], bisecting_results["Time"], label="Bisecting K-means Time", marker='o')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Time (seconds)")
plt.title("Computing Time vs Number of Clusters")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(kmeans_results["k"], kmeans_results["SSE"], label="K-means SSE", marker='o')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("SSE")
plt.title("SSE vs Number of Clusters (K-means)")
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize=(10, 5))
plt.plot(bisecting_results["k"], bisecting_results["SSE"], label="Bisecting K-means SSE", marker='o')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("SSE")
plt.title("SSE vs Number of Clusters (Bisecting K-means)")
plt.legend()
plt.grid()
plt.show()







