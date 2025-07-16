# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np
from euc_distances_cal_ID2693653 import *
from modified_neighbors_membership_ID2693653 import *

def modified_fuzzy_knn_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data, k, m):

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

    C1 = np.mean(train_split_data[train_split_true_labels == 0], axis=0)
    C2 = np.mean(train_split_data[train_split_true_labels == 1], axis=0)
    
    distance_to_centers = np.zeros((len(train_split_data), 2))
    for i in range(len(train_split_data)):
        distance_to_centers[i, 0] = np.sqrt(np.sum((C1 - train_split_data.iloc[i]) ** 2))
        distance_to_centers[i, 1] = np.sqrt(np.sum((C2 - train_split_data.iloc[i]) ** 2))


    test_predicted_labels = np.zeros(len(test_split_data))

    for k, neighbor_indices in enumerate(k_nearest_neighbors_indices):
        membership_values = np.zeros(2)
        for t in range(2):
            neighbors_membership = modified_neighbors_membership_ID2693653(distance_to_centers[neighbor_indices, :], t)
            distance_coefficient_vector =k_nearest_distances[k, :]**(-2/(m-1))
            membership_values[t] = np.dot(neighbors_membership, distance_coefficient_vector ) / np.sum(distance_coefficient_vector)

        max_membership_index = np.argmax(membership_values)
        test_predicted_labels[k] = max_membership_index


    return test_predicted_labels

