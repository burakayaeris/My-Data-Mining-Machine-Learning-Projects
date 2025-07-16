# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np
from folding_ID2693653 import *
from knn_classifier_ID2693653 import *

winconsin_df = pd.read_excel('Wisconsin Diagnostic Breast Cancer.xlsx')

# min-max normalization
winconsin_df_normal = (winconsin_df - winconsin_df.min()) / (winconsin_df.max() - winconsin_df.min())

num_folds = 5
max_k = 10

fold_list = folding_ID2693653(winconsin_df_normal, num_folds) # 5-folds (dataframes) in a list

# Saving folds to excel
for i, fold in enumerate(fold_list):
    fold.to_excel(f'Fold_{i + 1}.xlsx', index=False)

column_headers = [f'k={k}' for k in range(1, max_k + 1)]
row_headers = [f'Fold-{i}' for i in range(1, num_folds + 1)]
Error_Table_Df = pd.DataFrame(columns=column_headers, index=row_headers)

for i in range(num_folds):
    test_fold = fold_list[i]
    train_folds = []
    for j in range(num_folds):
        if j != i:
            train_folds.append(fold_list[j])
    training_dataset = pd.concat(train_folds, ignore_index=True)
    training_dataset_data = training_dataset.iloc[:, :-1]
    training_dataset_true_labels = training_dataset.iloc[:, -1]

    test_dataset_data = test_fold.iloc[:, :-1]
    test_dataset_true_labels = test_fold.iloc[:, -1]
    k_range = range(1, max_k + 1)
    error_rate_list = np.zeros(len(k_range))
    for index, k in enumerate(k_range):
        predicted_labels = knn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, k)
        test_error = np.mean(predicted_labels != test_dataset_true_labels)
        error_rate_list[index] = test_error
    Error_Table_Df.iloc[i] = error_rate_list

best_k_per_fold = []

for row_index, row in Error_Table_Df.iterrows():    
    best_k = row.astype(float).idxmin()  
    best_k_per_fold.append(best_k)
Error_Table_Df['Best k'] = best_k_per_fold

Error_Table_Df.to_excel('Error_Table_Df_Partd_ID2693653.xlsx', index=True)

    
    





