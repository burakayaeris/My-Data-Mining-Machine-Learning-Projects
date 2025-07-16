# Burak Ayaeriş 2693653

import numpy as np
from randomize_dataset_ID2693653 import *
def partition_dataset_ID2693653(df, train_split_ratio=0.8):
    randomized_df = randomize_dataset_ID2693653(df)
    train_split_size = round(len(randomized_df) * train_split_ratio)

    train_split_data = randomized_df.iloc[:train_split_size,:]
    test_split_data = randomized_df.iloc[train_split_size:,:]

    return train_split_data, test_split_data
