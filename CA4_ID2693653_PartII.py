# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from modified_fuzzy_knn_classifier_ID2693653 import *
from rnn_classifier_ID2693653 import *
from m_rnn_classifier_ID2693653 import *
from mknn_classifier_ID2693653 import *
from fuzzy_knn_classifier_ID2693653 import *

from folding_ID2693653 import *


# Part a-) 

# folds were created from the previous computing assignment

fold_list = []
# the fold dataframes in part-d (it was saved in excel format)
for i in range(1, 6):
    fold_list.append(pd.read_excel(f'Fold_{i}.xlsx'))

num_folds = 5
max_k = 10
m=2

column_headers = [f'k={k}' for k in range(1, max_k + 1)]
row_headers = [f'Fold-{i}' for i in range(1, num_folds + 1)]
Error_Table_Df = pd.DataFrame(columns=column_headers, index=row_headers)


# 1- Modified Fuzzy KNN Classifier
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
        predicted_labels = modified_fuzzy_knn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, k, m)
        test_error = np.mean(predicted_labels != test_dataset_true_labels)
        error_rate_list[index] = test_error
    Error_Table_Df.iloc[i] = error_rate_list

best_k_per_fold = []
best_error_per_fold = []

for row_index, row in Error_Table_Df.iterrows():    
    best_k = row.astype(float).idxmin()  
    best_k_per_fold.append(best_k)
    best_error = row.astype(float).min()
    best_error_per_fold.append(best_error)

Error_Table_Df['Best Error'] = best_error_per_fold
Error_Table_Df['Best k'] = best_k_per_fold

# best of best fold errors
best_of_best_error = Error_Table_Df['Best Error'].min()
Error_Table_Df['Best'] = best_of_best_error

# worst of best fold errors
worst_of_best_error = Error_Table_Df['Best Error'].max()
Error_Table_Df['Worst'] = worst_of_best_error

# average of best fold errors
average_of_best_error = Error_Table_Df['Best Error'].mean()
Error_Table_Df['Average'] = average_of_best_error 


Error_Table_Df.to_excel('Error_Table_Df_CA4_PartIIa_modified_fuzzy_ID2693653.xlsx', index=True)

# 2- RNN Classifier

r_range = np.linspace(0.01, 3, 30)
column_headers = [f'r={r}' for r in r_range]
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
    training_dataset_true_labels = training_dataset.iloc[:, -1].to_numpy()

    test_dataset_data = test_fold.iloc[:, :-1]
    test_dataset_true_labels = test_fold.iloc[:, -1].to_numpy()
    
    rnn_error_rate_list = np.zeros(len(r_range))
    
    for index, r in enumerate(r_range):
        predicted_labels = rnn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, r)
        test_error = np.mean(predicted_labels != test_dataset_true_labels)
        rnn_error_rate_list[index] = test_error
    
    Error_Table_Df.iloc[i] = rnn_error_rate_list
best_r_per_fold = []
best_r_error_per_fold = []
for row_index, row in Error_Table_Df.iterrows():    
    best_r = row.astype(float).idxmin()  
    best_r_per_fold.append(best_r)
    best_r_error = row.astype(float).min()
    best_r_error_per_fold.append(best_r_error)
Error_Table_Df['Best Error'] = best_r_error_per_fold
Error_Table_Df['Best r'] = best_r_per_fold
# best of best fold errors
best_of_best_r_error = Error_Table_Df['Best Error'].min()
Error_Table_Df['Best'] = best_of_best_r_error
# worst of best fold errors
worst_of_best_r_error = Error_Table_Df['Best Error'].max()
Error_Table_Df['Worst'] = worst_of_best_r_error
# average of best fold errors
average_of_best_r_error = Error_Table_Df['Best Error'].mean()
Error_Table_Df['Average'] = average_of_best_r_error
Error_Table_Df.to_excel('Error_Table_Df_CA4_PartIIa_rnn_ID2693653.xlsx', index=True)

# 3- m-RNN Classifier

r_range = np.linspace(0.01, 3, 30)
column_headers = [f'r={r}' for r in r_range]
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
    training_dataset_true_labels = training_dataset.iloc[:, -1].to_numpy()

    test_dataset_data = test_fold.iloc[:, :-1]
    test_dataset_true_labels = test_fold.iloc[:, -1].to_numpy()
    
    m_rnn_error_rate_list = np.zeros(len(r_range))
    
    for index, r in enumerate(r_range):
        predicted_labels = m_rnn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, r)
        test_error = np.mean(predicted_labels != test_dataset_true_labels)
        m_rnn_error_rate_list[index] = test_error
    
    Error_Table_Df.iloc[i] = m_rnn_error_rate_list
best_r_per_fold = []
best_r_error_per_fold = []
for row_index, row in Error_Table_Df.iterrows():    
    best_r = row.astype(float).idxmin()  
    best_r_per_fold.append(best_r)
    best_r_error = row.astype(float).min()
    best_r_error_per_fold.append(best_r_error)
Error_Table_Df['Best Error'] = best_r_error_per_fold
Error_Table_Df['Best r'] = best_r_per_fold
# best of best fold errors
best_of_best_r_error = Error_Table_Df['Best Error'].min()
Error_Table_Df['Best'] = best_of_best_r_error
# worst of best fold errors
worst_of_best_r_error = Error_Table_Df['Best Error'].max()
Error_Table_Df['Worst'] = worst_of_best_r_error
# average of best fold errors
average_of_best_r_error = Error_Table_Df['Best Error'].mean()
Error_Table_Df['Average'] = average_of_best_r_error
Error_Table_Df.to_excel('Error_Table_Df_CA4_PartIIa_m_rnn_ID2693653.xlsx', index=True)

# 4- Modified KNN Classifier

num_folds = 5
max_k = 10
m=2

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
best_error_per_fold = []
for row_index, row in Error_Table_Df.iterrows():    
    best_k = row.astype(float).idxmin()  
    best_k_per_fold.append(best_k)
    best_error = row.astype(float).min()
    best_error_per_fold.append(best_error)
Error_Table_Df['Best Error'] = best_error_per_fold
Error_Table_Df['Best k'] = best_k_per_fold
# best of best fold errors
best_of_best_error = Error_Table_Df['Best Error'].min()
Error_Table_Df['Best'] = best_of_best_error
# worst of best fold errors
worst_of_best_error = Error_Table_Df['Best Error'].max()
Error_Table_Df['Worst'] = worst_of_best_error
# average of best fold errors
average_of_best_error = Error_Table_Df['Best Error'].mean()
Error_Table_Df['Average'] = average_of_best_error
Error_Table_Df.to_excel('Error_Table_Df_CA4_PartIIa_mknn_ID2693653.xlsx', index=True)

# 5- Fuzzy KNN Classifier

num_folds = 5
max_k = 10
m=2

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
        predicted_labels = fuzzy_knn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, k, m)
        test_error = np.mean(predicted_labels != test_dataset_true_labels)
        error_rate_list[index] = test_error
    Error_Table_Df.iloc[i] = error_rate_list
best_k_per_fold = []
best_error_per_fold = []
for row_index, row in Error_Table_Df.iterrows():    
    best_k = row.astype(float).idxmin()  
    best_k_per_fold.append(best_k)
    best_error = row.astype(float).min()
    best_error_per_fold.append(best_error)
Error_Table_Df['Best Error'] = best_error_per_fold
Error_Table_Df['Best k'] = best_k_per_fold
# best of best fold errors
best_of_best_error = Error_Table_Df['Best Error'].min()
Error_Table_Df['Best'] = best_of_best_error
# worst of best fold errors
worst_of_best_error = Error_Table_Df['Best Error'].max()
Error_Table_Df['Worst'] = worst_of_best_error
# average of best fold errors
average_of_best_error = Error_Table_Df['Best Error'].mean()
Error_Table_Df['Average'] = average_of_best_error
Error_Table_Df.to_excel('Error_Table_Df_CA4_PartIIa_fuzzy_knn_ID2693653.xlsx', index=True)



# Part b-)


winconsin_df = pd.read_excel('Wisconsin Diagnostic Breast Cancer.xlsx')

# min-max normalization
winconsin_df_normal = (winconsin_df - winconsin_df.min()) / (winconsin_df.max() - winconsin_df.min())

num_folds = 5
max_k = 10
m = 2
for partition in range(5):
    fold_list = folding_ID2693653(winconsin_df_normal, num_folds) # 5-folds (dataframes) in a list

    # Saving folds to excel
    for i, fold in enumerate(fold_list):
        fold.to_excel(f'Partition_{partition + 1}_Fold_{i + 1}.xlsx', index=False)

    # 1- Modified Fuzzy KNN Classifier
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
            predicted_labels = modified_fuzzy_knn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, k, m)
            test_error = np.mean(predicted_labels != test_dataset_true_labels)
            error_rate_list[index] = test_error
        Error_Table_Df.iloc[i] = error_rate_list

    best_k_per_fold = []
    best_error_per_fold = []

    for row_index, row in Error_Table_Df.iterrows():    
        best_k = row.astype(float).idxmin()  
        best_k_per_fold.append(best_k)
        best_error = row.astype(float).min()
        best_error_per_fold.append(best_error)

    Error_Table_Df['Best Error'] = best_error_per_fold
    Error_Table_Df['Best k'] = best_k_per_fold

    # best of best fold errors
    best_of_best_error = Error_Table_Df['Best Error'].min()
    Error_Table_Df['Best'] = best_of_best_error

    # worst of best fold errors
    worst_of_best_error = Error_Table_Df['Best Error'].max()
    Error_Table_Df['Worst'] = worst_of_best_error

    # average of best fold errors
    average_of_best_error = Error_Table_Df['Best Error'].mean()
    Error_Table_Df['Average'] = average_of_best_error 

    Error_Table_Df.to_excel(f'Error_Table_Df_CA4_PartIIa_modified_fuzzy_ID2693653_Partition_{partition + 1}.xlsx', index=True)

    # 2- RNN Classifier
    r_range = np.linspace(0.01, 3, 30)
    column_headers = [f'r={r}' for r in r_range]
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
        training_dataset_true_labels = training_dataset.iloc[:, -1].to_numpy()

        test_dataset_data = test_fold.iloc[:, :-1]
        test_dataset_true_labels = test_fold.iloc[:, -1].to_numpy()
        
        rnn_error_rate_list = np.zeros(len(r_range))
        
        for index, r in enumerate(r_range):
            predicted_labels = rnn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, r)
            test_error = np.mean(predicted_labels != test_dataset_true_labels)
            rnn_error_rate_list[index] = test_error
        
        Error_Table_Df.iloc[i] = rnn_error_rate_list

    best_r_per_fold = []
    best_r_error_per_fold = []
    for row_index, row in Error_Table_Df.iterrows():    
        best_r = row.astype(float).idxmin()  
        best_r_per_fold.append(best_r)
        best_r_error = row.astype(float).min()
        best_r_error_per_fold.append(best_r_error)

    Error_Table_Df['Best Error'] = best_r_error_per_fold
    Error_Table_Df['Best r'] = best_r_per_fold

    # best of best fold errors
    best_of_best_r_error = Error_Table_Df['Best Error'].min()
    Error_Table_Df['Best'] = best_of_best_r_error

    # worst of best fold errors
    worst_of_best_r_error = Error_Table_Df['Best Error'].max()
    Error_Table_Df['Worst'] = worst_of_best_r_error

    # average of best fold errors
    average_of_best_r_error = Error_Table_Df['Best Error'].mean()
    Error_Table_Df['Average'] = average_of_best_r_error

    Error_Table_Df.to_excel(f'Error_Table_Df_CA4_PartIIa_rnn_ID2693653_Partition_{partition + 1}.xlsx', index=True)

    # 3- m-RNN Classifier
    r_range = np.linspace(0.01, 3, 30)
    column_headers = [f'r={r}' for r in r_range]
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
        training_dataset_true_labels = training_dataset.iloc[:, -1].to_numpy()

        test_dataset_data = test_fold.iloc[:, :-1]
        test_dataset_true_labels = test_fold.iloc[:, -1].to_numpy()
        
        m_rnn_error_rate_list = np.zeros(len(r_range))
        
        for index, r in enumerate(r_range):
            predicted_labels = m_rnn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, r)
            test_error = np.mean(predicted_labels != test_dataset_true_labels)
            m_rnn_error_rate_list[index] = test_error
        
        Error_Table_Df.iloc[i] = m_rnn_error_rate_list

    best_r_per_fold = []
    best_r_error_per_fold = []
    for row_index, row in Error_Table_Df.iterrows():    
        best_r = row.astype(float).idxmin()  
        best_r_per_fold.append(best_r)
        best_r_error = row.astype(float).min()
        best_r_error_per_fold.append(best_r_error)

    Error_Table_Df['Best Error'] = best_r_error_per_fold
    Error_Table_Df['Best r'] = best_r_per_fold

    # best of best fold errors
    best_of_best_r_error = Error_Table_Df['Best Error'].min()
    Error_Table_Df['Best'] = best_of_best_r_error

    # worst of best fold errors
    worst_of_best_r_error = Error_Table_Df['Best Error'].max()
    Error_Table_Df['Worst'] = worst_of_best_r_error

    # average of best fold errors
    average_of_best_r_error = Error_Table_Df['Best Error'].mean()
    Error_Table_Df['Average'] = average_of_best_r_error

    Error_Table_Df.to_excel(f'Error_Table_Df_CA4_PartIIa_m_rnn_ID2693653_Partition_{partition + 1}.xlsx', index=True)

    # 4- Modified KNN Classifier
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
    best_error_per_fold = []
    for row_index, row in Error_Table_Df.iterrows():    
        best_k = row.astype(float).idxmin()  
        best_k_per_fold.append(best_k)
        best_error = row.astype(float).min()
        best_error_per_fold.append(best_error)

    Error_Table_Df['Best Error'] = best_error_per_fold
    Error_Table_Df['Best k'] = best_k_per_fold

    # best of best fold errors
    best_of_best_error = Error_Table_Df['Best Error'].min()
    Error_Table_Df['Best'] = best_of_best_error

    # worst of best fold errors
    worst_of_best_error = Error_Table_Df['Best Error'].max()
    Error_Table_Df['Worst'] = worst_of_best_error

    # average of best fold errors
    average_of_best_error = Error_Table_Df['Best Error'].mean()
    Error_Table_Df['Average'] = average_of_best_error

    Error_Table_Df.to_excel(f'Error_Table_Df_CA4_PartIIa_mknn_ID2693653_Partition_{partition + 1}.xlsx', index=True)

    # 5- Fuzzy KNN Classifier
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
            predicted_labels = fuzzy_knn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, k, m)
            test_error = np.mean(predicted_labels != test_dataset_true_labels)
            error_rate_list[index] = test_error
        Error_Table_Df.iloc[i] = error_rate_list

    best_k_per_fold = []
    best_error_per_fold = []
    for row_index, row in Error_Table_Df.iterrows():    
        best_k = row.astype(float).idxmin()  
        best_k_per_fold.append(best_k)
        best_error = row.astype(float).min()
        best_error_per_fold.append(best_error)

    Error_Table_Df['Best Error'] = best_error_per_fold
    Error_Table_Df['Best k'] = best_k_per_fold

    # best of best fold errors
    best_of_best_error = Error_Table_Df['Best Error'].min()
    Error_Table_Df['Best'] = best_of_best_error

    # worst of best fold errors
    worst_of_best_error = Error_Table_Df['Best Error'].max()
    Error_Table_Df['Worst'] = worst_of_best_error

    # average of best fold errors
    average_of_best_error = Error_Table_Df['Best Error'].mean()
    Error_Table_Df['Average'] = average_of_best_error

    Error_Table_Df.to_excel(f'Error_Table_Df_CA4_PartIIa_fuzzy_knn_ID2693653_Partition_{partition + 1}.xlsx', index=True)