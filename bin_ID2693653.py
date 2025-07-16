# Burak Ayaeriş 2693653

import numpy as np
import pandas as pd

# modified for PartIII

def bin_ID2693653(data, num_bins, skewness_parameter):
    data_binned = data.copy()
    columns_to_bin = ['Age', 'Experience', 'Income', 'CCAvg', 'Mortgage']

    for column in columns_to_bin:
        skew = data[column].skew()
        if skew > skewness_parameter:
            try:
                data_binned[column] = pd.qcut(data[column], q=num_bins, duplicates='drop')
                actual_bins = len(data_binned[column].cat.categories)
                labels = [str(i+1) for i in range(actual_bins)]
                data_binned[column] = pd.qcut(data[column], q=num_bins, labels=labels, duplicates='drop')
            except ValueError:
                data_binned[column] = pd.cut(data[column], bins=num_bins)
                actual_bins = len(data_binned[column].cat.categories)
                labels = [str(i+1) for i in range(actual_bins)]
                data_binned[column] = pd.cut(data[column], bins=num_bins, labels=labels)
        else:
            data_binned[column] = pd.cut(data[column], bins=num_bins)
            actual_bins = len(data_binned[column].cat.categories)
            labels = [str(i+1) for i in range(actual_bins)]
            data_binned[column] = pd.cut(data[column], bins=num_bins, labels=labels)
        
    return data_binned







