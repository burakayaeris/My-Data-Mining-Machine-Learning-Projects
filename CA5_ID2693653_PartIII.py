# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np
from folding_ID2693653 import folding_ID2693653
from knn_classifier_ID2693653 import knn_classifier_ID2693653
from mknn_classifier_ID2693653 import mknn_classifier_ID2693653
from fuzzy_knn_classifier_ID2693653 import fuzzy_knn_classifier_ID2693653
from rnn_classifier_ID2693653 import rnn_classifier_ID2693653

from bin_ID2693653 import bin_ID2693653
from naive_bayes_classifier_ID2693653 import naive_bayes_classifier_ID2693653


universal_bank_df = pd.read_excel("UniversalBank.xlsx", sheet_name="Data")

num_folds = 5
m=2
max_k = 10
"""
fold_list = folding_ID2693653(universal_bank_df, num_folds)

for i, fold in enumerate(fold_list):
    fold.to_excel(f'PartIII_Fold_{i + 1}.xlsx', index=False)
"""
# after saved, folds are fixed
fold_list = []
for i in range(1, 6):
    fold_list.append(pd.read_excel(f'PartIII_Fold_{i}.xlsx'))

column_headers = [f'k={k}' for k in range(1, max_k + 1)]
row_headers = [f'Fold-{i}' for i in range(1, num_folds + 1)]
Accuracy_Table_Df = pd.DataFrame(columns=column_headers, index=row_headers)


### Euclidean distance function is modified even though it has the same name as before for a new distance measure

# KNN 
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
    accuracy_list = np.zeros(len(k_range))



    for index, k in enumerate(k_range):
        predicted_labels = knn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, k)
        accuracy = np.mean(predicted_labels == test_dataset_true_labels)
        accuracy_list[index] = accuracy
    Accuracy_Table_Df.iloc[i] = accuracy_list

best_k_per_fold = []
best_accuracy_per_fold = []
for row_index, row in Accuracy_Table_Df.iterrows():    
    best_k = row.astype(float).idxmax()  
    best_k_per_fold.append(best_k)
    best_accuracy = row.astype(float).max()  
    best_accuracy_per_fold.append(best_accuracy)

Accuracy_Table_Df['Best Accuracy'] = best_accuracy_per_fold
Accuracy_Table_Df['Best k'] = best_k_per_fold

best_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].max()  
Accuracy_Table_Df['Best'] = best_of_best_accuracy

worst_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].min()  
Accuracy_Table_Df['Worst'] = worst_of_best_accuracy

average_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].mean()
Accuracy_Table_Df['Average'] = average_of_best_accuracy

Accuracy_Table_Df.to_excel('Accuracy_Table_Df_CA5_PartIII_KNN_ID2693653.xlsx', index=True)

column_headers = [f'k={k}' for k in range(1, max_k + 1)]
row_headers = [f'Fold-{i}' for i in range(1, num_folds + 1)]
Accuracy_Table_Df = pd.DataFrame(columns=column_headers, index=row_headers)

# Modified KNN
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
    accuracy_list = np.zeros(len(k_range))
    for index, k in enumerate(k_range):
        predicted_labels = mknn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, k)
        accuracy = np.mean(predicted_labels == test_dataset_true_labels)
        accuracy_list[index] = accuracy
    Accuracy_Table_Df.iloc[i] = accuracy_list

best_k_per_fold = []
best_accuracy_per_fold = []
for row_index, row in Accuracy_Table_Df.iterrows():    
    best_k = row.astype(float).idxmax()  
    best_k_per_fold.append(best_k)
    best_accuracy = row.astype(float).max()  
    best_accuracy_per_fold.append(best_accuracy)

Accuracy_Table_Df['Best Accuracy'] = best_accuracy_per_fold
Accuracy_Table_Df['Best k'] = best_k_per_fold

best_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].max()  
Accuracy_Table_Df['Best'] = best_of_best_accuracy

worst_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].min()  
Accuracy_Table_Df['Worst'] = worst_of_best_accuracy

average_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].mean()
Accuracy_Table_Df['Average'] = average_of_best_accuracy

Accuracy_Table_Df.to_excel('Accuracy_Table_Df_CA5_PartIII_MKNN_ID2693653.xlsx', index=True)

column_headers = [f'k={k}' for k in range(1, max_k + 1)]
row_headers = [f'Fold-{i}' for i in range(1, num_folds + 1)]
Accuracy_Table_Df = pd.DataFrame(columns=column_headers, index=row_headers)

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
    accuracy_list = np.zeros(len(k_range))
    for index, k in enumerate(k_range):
        predicted_labels = fuzzy_knn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, k, m)
        accuracy = np.mean(predicted_labels == test_dataset_true_labels)
        accuracy_list[index] = accuracy
    Accuracy_Table_Df.iloc[i] = accuracy_list

best_k_per_fold = []
best_accuracy_per_fold = []
for row_index, row in Accuracy_Table_Df.iterrows():    
    best_k = row.astype(float).idxmax()  
    best_k_per_fold.append(best_k)
    best_accuracy = row.astype(float).max()  
    best_accuracy_per_fold.append(best_accuracy)

Accuracy_Table_Df['Best Accuracy'] = best_accuracy_per_fold
Accuracy_Table_Df['Best k'] = best_k_per_fold

best_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].max()  
Accuracy_Table_Df['Best'] = best_of_best_accuracy

worst_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].min()  
Accuracy_Table_Df['Worst'] = worst_of_best_accuracy

average_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].mean()
Accuracy_Table_Df['Average'] = average_of_best_accuracy

Accuracy_Table_Df.to_excel('Accuracy_Table_Df_CA5_PartIII_FUZZY_KNN_ID2693653.xlsx', index=True)


r_range = np.linspace(0.01, 1, 10)
column_headers = [f'r={r}' for r in r_range]
row_headers = [f'Fold-{i}' for i in range(1, num_folds + 1)]
Accuracy_Table_Df = pd.DataFrame(columns=column_headers, index=row_headers)

# RNN

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
    accuracy_list = np.zeros(len(r_range))
    for index, r in enumerate(r_range):
        predicted_labels = rnn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, r)
        accuracy = np.mean(predicted_labels == test_dataset_true_labels)
        accuracy_list[index] = accuracy
    Accuracy_Table_Df.iloc[i] = accuracy_list

best_r_per_fold = []
best_accuracy_per_fold = []
for row_index, row in Accuracy_Table_Df.iterrows():    
    best_r = row.astype(float).idxmax()  
    best_r_per_fold.append(best_r)
    best_accuracy = row.astype(float).max()  
    best_accuracy_per_fold.append(best_accuracy)

Accuracy_Table_Df['Best Accuracy'] = best_accuracy_per_fold
Accuracy_Table_Df['Best r'] = best_r_per_fold

best_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].max()  
Accuracy_Table_Df['Best'] = best_of_best_accuracy

worst_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].min()  
Accuracy_Table_Df['Worst'] = worst_of_best_accuracy

average_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].mean()
Accuracy_Table_Df['Average'] = average_of_best_accuracy

Accuracy_Table_Df.to_excel('Accuracy_Table_Df_CA5_PartIII_RNN_ID2693653.xlsx', index=True)


# Naive Bayes
bin_range = [2, 3, 4]
column_headers = [f'bin={bin}' for bin in bin_range]
row_headers = [f'Fold-{i}' for i in range(1, num_folds + 1)]
Accuracy_Table_Df = pd.DataFrame(columns=column_headers, index=row_headers)

for i in range(num_folds):
    test_fold = fold_list[i]
    train_folds = []
    for j in range(num_folds):
        if j != i:
            train_folds.append(fold_list[j])
    
    training_dataset = pd.concat(train_folds, ignore_index=True)
    
    accuracies = []
    for num_bins in bin_range:
        training_dataset_binned = bin_ID2693653(training_dataset, num_bins, 1)
        test_fold_binned = bin_ID2693653(test_fold, num_bins, 1)
        
        training_dataset_data = training_dataset_binned.iloc[:, :-1]
        training_dataset_true_labels = training_dataset_binned.iloc[:, -1]

        test_dataset_data = test_fold_binned.iloc[:, :-1]
        test_dataset_true_labels = test_fold_binned.iloc[:, -1]

        predicted_labels = naive_bayes_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data)
        accuracy = np.mean(predicted_labels == test_dataset_true_labels)
        accuracies.append(accuracy)
 
    Accuracy_Table_Df.iloc[i] = accuracies

for bin_num in bin_range:
    col_name = f'bin={bin_num}'
    best_accuracy = Accuracy_Table_Df[col_name].max()
    worst_accuracy = Accuracy_Table_Df[col_name].min()
    avg_accuracy = Accuracy_Table_Df[col_name].mean()
    
    Accuracy_Table_Df[f'Best_{col_name}'] = best_accuracy
    Accuracy_Table_Df[f'Worst_{col_name}'] = worst_accuracy
    Accuracy_Table_Df[f'Average_{col_name}'] = avg_accuracy

Accuracy_Table_Df.to_excel('Accuracy_Table_Df_CA5_PartIII_NaiveBayes_ID2693653.xlsx', index=True)


# Naive Rule (for benchmarking)

row_headers = [f'Fold-{i}' for i in range(1, num_folds + 1)]
Accuracy_Table_Df = pd.DataFrame(columns=['Accuracy'], index=row_headers)

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
    
    values, counts = np.unique(training_dataset_true_labels, return_counts=True)
    majority_label = values[np.argmax(counts)]
    predicted_labels = [majority_label] * len(test_dataset_data)

    accuracy = np.mean(predicted_labels == test_dataset_true_labels)
    Accuracy_Table_Df.iloc[i] = accuracy

best_accuracy_per_fold = Accuracy_Table_Df['Accuracy'].values
Accuracy_Table_Df['Best Accuracy'] = best_accuracy_per_fold
best_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].max()  
Accuracy_Table_Df['Best'] = best_of_best_accuracy
worst_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].min()  
Accuracy_Table_Df['Worst'] = worst_of_best_accuracy
average_of_best_accuracy = Accuracy_Table_Df['Best Accuracy'].mean()
Accuracy_Table_Df['Average'] = average_of_best_accuracy

Accuracy_Table_Df.to_excel('Accuracy_Table_Df_CA5_PartIII_NaiveRule_ID2693653.xlsx', index=True)
