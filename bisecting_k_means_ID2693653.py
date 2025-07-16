# Burak Ayaeriş 2693653


import numpy as np
from kmeans_ID2693653 import *  
from math import inf

def bisecting_k_means(derma_array, k, num_initializations):
    cluster_list = [np.arange(len(derma_array))]
    cluster_sse_list = [np.sum((derma_array[c,:] - derma_array[c,:].mean(axis=0))**2) for c in cluster_list]

    while len(cluster_list) < k:
    
        cluster_idx_w_max_sse = np.argmax(cluster_sse_list)
        data_to_split = derma_array[cluster_list[cluster_idx_w_max_sse], :]

        best_sse = inf
        best_split = None
        best_sse_array = None


        for _ in range(num_initializations):
            nearest_center_indices, sse_array, total_sse, iteration = k_means(data_to_split, 2)
            if total_sse < best_sse:
                best_sse = total_sse
                best_split = nearest_center_indices.copy()
                best_sse_array = sse_array.copy()

        c_new1 = cluster_list[cluster_idx_w_max_sse][best_split == 0]
        c_new2 = cluster_list[cluster_idx_w_max_sse][best_split == 1]
   
        cluster_list[cluster_idx_w_max_sse] = c_new1
        cluster_list.append(c_new2)

        cluster_sse_list[cluster_idx_w_max_sse] = best_sse_array[0]
        cluster_sse_list.append(best_sse_array[1])


    cluster_assignments = np.zeros(derma_array.shape[0], dtype=int)
    for cluster_idx, indices in enumerate(cluster_list):
        cluster_assignments[indices] = cluster_idx

    sse_array = np.asarray(cluster_sse_list)
    return cluster_assignments, sse_array, float(np.sum(sse_array))
