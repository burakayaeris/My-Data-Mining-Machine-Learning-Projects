# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np
from euc_distances_cal_ID2693653 import *

def mknn_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data, k):
    # distance between test and train data
    euc_distances = euc_distances_cal_ID2693653(train_split_data, test_split_data) # #test * #train
    neighbors_indices = np.argsort(euc_distances, axis=1)
    k_nearest_neighbors_indices = neighbors_indices[:, :k]

    k_nearest_distances = np.zeros((len(test_split_data), k))
    for i in range(len(test_split_data)):
        for j in range(k):
            k_nearest_distances[i,j] = euc_distances[i,k_nearest_neighbors_indices[i,j]] 

    k_nearest_label_array = np.zeros((len(test_split_data), k)) 
    for i in range(len(test_split_data)):
        for j in range(k):
            k_nearest_label_array[i,j] = train_split_true_labels[k_nearest_neighbors_indices[i,j]] 
   
    k_nearest_weights = np.zeros((len(test_split_data), k))
    for i in range(len(test_split_data)):
        for j in range(k):
            if k_nearest_distances[i,j] == k_nearest_distances[i,0]:
                k_nearest_weights[i,j] = 1
            else:
                denominator = k_nearest_distances[i,-1] - k_nearest_distances[i,0]
                if denominator == 0:
                    k_nearest_weights[i,j] = 1
                else:
                    weight = (k_nearest_distances[i,-1] - k_nearest_distances[i,j]) / denominator
                    k_nearest_weights[i,j] = max(0, min(1, weight)) 
    
    test_predicted_labels = np.zeros(len(test_split_data))
    for k, labels in enumerate(k_nearest_label_array):
        unique_labels = np.unique(labels)
        weight_sum = np.zeros(len(unique_labels))
        for label_index, label in enumerate(unique_labels):
            label_indices = np.where(labels == label)[0]
            weight_sum[label_index] = np.sum(k_nearest_weights[k, label_indices])
        
        max_weight = np.max(weight_sum) 
        class_candidates = unique_labels[weight_sum == max_weight]
        if len(class_candidates) > 1:
            test_predicted_labels[k] = np.random.choice(class_candidates)
        else:
            test_predicted_labels[k] = class_candidates[0]
        

    return test_predicted_labels

