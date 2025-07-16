# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np
from euc_distances_cal_ID2693653 import *
from knn_classifier_ID2693653 import *

def rnn_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data, k, r):

    # distance between test and train data
    euc_distances = euc_distances_cal_ID2693653(train_split_data, test_split_data) # #test * #train
    neighbors_indices = np.argsort(euc_distances, axis=1)
    
    test_predicted_labels = np.zeros(len(test_split_data))

    for i in range(len(test_split_data)):
        neighborhood_indices = np.where(euc_distances[i] <= r)[0]
    
        if len(neighborhood_indices) == 0:
            unique_labels, counts = np.unique(train_split_true_labels, return_counts=True)
            test_predicted_labels[i] = unique_labels[np.argmax(counts)]
        else:
            neighborhood_data = train_split_data.iloc[neighborhood_indices]
            neighborhood_labels = train_split_true_labels.iloc[neighborhood_indices]
            knn_predicted_labels = knn_classifier_ID2693653(neighborhood_data, neighborhood_labels, test_split_data.iloc[[i]], k)
            test_predicted_labels[i] = knn_predicted_labels[0]
            
    return test_predicted_labels