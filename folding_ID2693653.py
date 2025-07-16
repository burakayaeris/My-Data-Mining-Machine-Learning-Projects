# Burak Ayaeriş 2693653
from randomize_dataset_ID2693653 import *

def folding_ID2693653(df, num_folds):
    folds = []
    randomized_df = randomize_dataset_ID2693653(df)
    n = len(randomized_df)
    fold_size = n // num_folds
    remainder = n % num_folds
    low_index = 0
    for i in range(num_folds):
        if i < remainder:
            high_index = low_index + fold_size + 1
        else:
            high_index = low_index + fold_size
        folds.append(randomized_df.iloc[low_index:high_index, :])
        low_index = high_index
    return folds
