# Burak Ayaeriş 2693653

import numpy as np

from init_centers_ID2693653 import *

def k_means(derma_array, k):
    
    num_data_points = derma_array.shape[0]
    num_attributes = derma_array.shape[1]

    center_points = init_centers(derma_array, k)
    
    center_points_reshaped = center_points.reshape(1, k, num_attributes) # broadcasting 
    center_points_reshaped_updated = center_points_reshaped.copy()
    derma_array_reshaped = derma_array.reshape(num_data_points, 1, num_attributes)

    iteration = 0

    while True:
        iteration += 1
       
        distances = np.sqrt(np.sum((derma_array_reshaped - center_points_reshaped) ** 2, axis=2)) # 366 * k numpy array
        nearest_center_indices = np.argmin(distances, axis=1)
        for cluster in range(k):
            cluster_points = derma_array_reshaped[nearest_center_indices == cluster,:,:]
            
            
            if len(cluster_points) == 0:
                nearest_point_index = distances[:, cluster].argmin(axis=0)
                center_points_reshaped_updated[0, cluster, :] = derma_array_reshaped[nearest_point_index,0,:] # the nearest point to the center of empty cluster is assigned to the empty cluster

            else:
                center_points_reshaped_updated[0, cluster, :] = np.mean(cluster_points, axis=0)  # center update
            
            
        # It will stop if the center points do not change anymore
        if np.all(center_points_reshaped == center_points_reshaped_updated):
            break

        center_points_reshaped = center_points_reshaped_updated.copy()

    # Sum of squared errors (SSE) array 
    sse_array = np.zeros(k)
    for a in range(k):
        sse_array[a] = np.sum(np.square(distances[nearest_center_indices == a, a]))
    total_sse = float(np.sum(sse_array))

    return nearest_center_indices, sse_array, total_sse, iteration






            