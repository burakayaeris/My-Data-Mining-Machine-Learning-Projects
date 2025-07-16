# Burak Ayaeriş 2693653

import numpy as np
import pandas as pd
from euc_distances_cal_ID2693653 import *
from mknn_classifier_ID2693653 import *

def m_rnn_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data, r):
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
            k = len(neighborhood_indices)
            neighborhood_data = train_split_data.iloc[neighborhood_indices]
            neighborhood_labels = train_split_true_labels[neighborhood_indices]
            mknn_predicted_labels = mknn_classifier_ID2693653(neighborhood_data, neighborhood_labels, test_split_data.iloc[[i]], k)
            test_predicted_labels[i] = mknn_predicted_labels[0]

    return test_predicted_labels