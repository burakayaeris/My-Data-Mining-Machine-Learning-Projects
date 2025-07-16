# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np

def neighbors_membership_ID2693653(label, k_labels_of_test_point):
    
    neighbors_membership_array = np.zeros(len(k_labels_of_test_point))
    for i in range(len(k_labels_of_test_point)):
        if k_labels_of_test_point[i] == label:
            neighbors_membership_array[i] = 1
        else:
            neighbors_membership_array[i] = 0
            
    return neighbors_membership_array
