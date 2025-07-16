# Burak Ayaeriş 2693653

import numpy as np

def init_centers(derma_array, k):
    # Selecting k random indices and using them to initialize the centers
    center_indices = np.random.choice(derma_array.shape[0], k, replace=False)
    centers = derma_array[center_indices,:]
    centers = centers.astype(np.float64)
 
    return centers

