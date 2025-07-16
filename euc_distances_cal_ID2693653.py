# Burak Ayaeriş 2693653
import pandas as pd
import numpy as np

def euc_distances_cal_ID2693653(train_split_data, test_split_data):
    # Types of attributes I chose to use
    # Numeric attributes; Age, Experience, Income, Family, CCAvg, Mortgage
    # Ordinal attributes; Education
    # Binary attributes; Securities Account, CD Account, Online, CreditCard

    numeric_cols = ['Age', 'Experience', 'Income', 'Family', 'CCAvg', 'Mortgage']
    ordinal_cols = ['Education']
    binary_cols = ['Securities Account', 'CD Account', 'Online', 'CreditCard']

    train_numeric = train_split_data[numeric_cols].values
    test_numeric = test_split_data[numeric_cols].values

    train_ordinal = train_split_data[ordinal_cols].values
    test_ordinal = test_split_data[ordinal_cols].values
    train_binary = train_split_data[binary_cols].values
    test_binary = test_split_data[binary_cols].values
    numeric_ranges = train_numeric.max(axis=0) - train_numeric.min(axis=0)
    numeric_ranges = np.where(numeric_ranges == 0, 1e-10, numeric_ranges) 

    ordinal_ranks = np.array([len(np.unique(train_ordinal[:, i])) for i in range(len(ordinal_cols))])
    ordinal_ranks = np.maximum(ordinal_ranks, 2) 
    distances = np.zeros((len(test_split_data), len(train_split_data)))
    numeric_dist = np.abs(test_numeric[:, np.newaxis, :] - train_numeric[np.newaxis, :, :])
    numeric_dist = numeric_dist / numeric_ranges[np.newaxis, np.newaxis, :]

    ordinal_dist = np.abs(test_ordinal[:, np.newaxis, :] - train_ordinal[np.newaxis, :, :])
    ordinal_dist = ordinal_dist / (ordinal_ranks[np.newaxis, np.newaxis, :] - 1)
    binary_dist = (test_binary[:, np.newaxis, :] != train_binary[np.newaxis, :, :]).astype(float)

    all_distances = np.concatenate([numeric_dist, ordinal_dist, binary_dist], axis=2)
    weights = (test_split_data.values[:, np.newaxis, :] != 0) | (train_split_data.values[np.newaxis, :, :] != 0)
    
    weighted_sum = np.sum(all_distances * weights, axis=2)
    weight_sum = np.sum(weights, axis=2)
    
    distances = np.divide(weighted_sum, weight_sum, out=np.zeros_like(weighted_sum), where=weight_sum!=0)


    return distances

