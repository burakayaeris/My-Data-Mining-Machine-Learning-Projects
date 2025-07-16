# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mknn_classifier_ID2693653 import *

fold_list = []
# the fold dataframes in part-d (it was saved in excel format)
for i in range(1, 6):
    fold_list.append(pd.read_excel(f'Fold_{i}.xlsx'))

num_folds = 5
max_k = 10

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
        predicted_labels = mknn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, k)
        test_error = np.mean(predicted_labels != test_dataset_true_labels)
        error_rate_list[index] = test_error
    Error_Table_Df.iloc[i] = error_rate_list

best_k_per_fold = []

for row_index, row in Error_Table_Df.iterrows():    
    best_k = row.astype(float).idxmin()  
    best_k_per_fold.append(best_k)
Error_Table_Df['Best k'] = best_k_per_fold

Error_Table_Df.to_excel('Error_Table_Df_Partf_ID2693653.xlsx', index=True)


for i in range(num_folds):
    plt.figure(figsize=(8, 5))  # Plots the error rates vs k for each fold
    plt.plot(list(range(1, max_k + 1)), list(Error_Table_Df.iloc[i, :-1]), marker='o', label=f'Fold {i + 1}')
    plt.plot(list(range(1, max_k + 1)), list(Error_Table_Df.iloc[i, :-1]), marker='o')
    plt.title(f'Error Rate vs k for Fold {i + 1}')
    plt.xlabel('k')
    plt.ylabel('Error Rate')
    plt.xticks(list(range(1, max_k + 1)))
    plt.grid()
    plt.show()
