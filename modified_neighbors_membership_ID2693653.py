# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np

def modified_neighbors_membership_ID2693653(distance_to_centers, class_index):
    
    neighbors_membership_array = np.zeros(len(distance_to_centers))
    small_value = 1e-10

    for i, distance in enumerate(distance_to_centers):

        

        neighbors_membership_array[i]=(1/(distance[class_index]+small_value))/((1/(distance[0]+small_value)) + (1/(distance[1]+small_value)))

    
    return neighbors_membership_array
