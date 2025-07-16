# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np
from euc_distances_cal_ID2693653 import *

def knn_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data, k):
    # distance between test and train data
    euc_distances = euc_distances_cal_ID2693653(train_split_data, test_split_data) # #test * #train
    neighbors_indices = np.argsort(euc_distances, axis=1)
    k_nearest_neighbors_indices = neighbors_indices[:, :k]

    k_nearest_label_array = np.zeros((len(test_split_data), k)) 
    for i in range(len(test_split_data)):
        for j in range(k):
            k_nearest_label_array[i,j] = train_split_true_labels[k_nearest_neighbors_indices[i,j]] # labels of k nearest neighbors of each test data point in numpy array
    
    test_predicted_labels = np.zeros(len(test_split_data))

    for i, labels in enumerate(k_nearest_label_array):
        unique_labels, counts = np.unique(labels, return_counts=True)   
        max_count = np.max(counts)
        candidates = unique_labels[counts == max_count]
        if len(candidates) > 1: # tie 
            chosen = np.random.choice(candidates)
            test_predicted_labels[i] = chosen
        else:
            test_predicted_labels[i] = candidates[0]

    return test_predicted_labels