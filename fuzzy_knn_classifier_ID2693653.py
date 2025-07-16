# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np
from euc_distances_cal_ID2693653 import *
from neighbors_membership_ID2693653 import *

def fuzzy_knn_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data, k, m):

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

    test_predicted_labels = np.zeros(len(test_split_data))


    for k, labels in enumerate(k_nearest_label_array):
        unique_labels = np.unique(labels)
        membership_values = np.zeros(len(unique_labels))
        for label_index, label in enumerate(unique_labels):
            #label_indices = np.where(labels == label)[0]
            neighbors_membership = neighbors_membership_ID2693653(label, k_nearest_label_array[k])
            distance_coefficient_vector =k_nearest_distances[k, :]**(-2/(m-1))
            membership_values[label_index] = np.dot(neighbors_membership, distance_coefficient_vector ) / np.sum(distance_coefficient_vector)
        max_membership_index = np.argmax(membership_values)

        test_predicted_labels[k] = unique_labels[max_membership_index]


    return test_predicted_labels

