# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from partition_dataset_ID2693653 import *
from modified_fuzzy_knn_classifier_ID2693653 import *
from rnn_classifier_ID2693653 import *
from m_rnn_classifier_ID2693653 import *


# Part a-)

#winconsin_df = pd.read_excel('Wisconsin Diagnostic Breast Cancer.xlsx')

# min-max normalization
#winconsin_df_normal = (winconsin_df - winconsin_df.min()) / (winconsin_df.max() - winconsin_df.min())

#train_split, test_split = partition_dataset_ID2693653(winconsin_df_normal)

#train_split_data = train_split.iloc[:,:-1]
#train_split_true_labels = train_split.iloc[:,-1]

#test_split_data = test_split.iloc[:,:-1]
#test_split_true_labels = test_split.iloc[:,-1]

# saving partitioned datasets to excel files
#train_split_data.to_excel('train_split_data_ID2693653.xlsx', index=False)
#train_split_true_labels.to_excel('train_split_true_labels_ID2693653.xlsx', index=False)
#test_split_data.to_excel('test_split_data_ID2693653.xlsx', index=False)
#test_split_true_labels.to_excel('test_split_true_labels_ID2693653.xlsx', index=False)

train_split_data = pd.read_excel('train_split_data_ID2693653.xlsx')
train_split_true_labels = pd.read_excel('train_split_true_labels_ID2693653.xlsx').iloc[:,0].to_numpy()
test_split_data = pd.read_excel('test_split_data_ID2693653.xlsx')
test_split_true_labels = pd.read_excel('test_split_true_labels_ID2693653.xlsx').iloc[:,0].to_numpy()

# From the previous coding assignment, the best k value was found to be 9 in fuzzy k-NN algorithm.
k = 9

m_range = range(2, 9)

fuzzy_knn_m_error_rate_list = np.zeros(len(m_range))

for index, m in enumerate(m_range):
    predicted_labels = modified_fuzzy_knn_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data, k, m)
    test_error = np.mean(predicted_labels != test_split_true_labels)
    fuzzy_knn_m_error_rate_list[index] = test_error

plt.plot(list(m_range), fuzzy_knn_m_error_rate_list, label="Fuzzy KNN Error Rate", marker='o', linestyle='-', color='red')
plt.title('Error Rate vs m')
plt.xlabel('m')
plt.ylabel('Error Rate')
plt.xticks(list(m_range))
plt.legend()
plt.grid()
plt.show()

fuzzy_knn_m_error_rates_df = pd.DataFrame({
    'm': m_range,
    'Error Rate': fuzzy_knn_m_error_rate_list
})

fuzzy_knn_m_error_rates_df.to_excel('Fuzzy_KNN_m_Error_Rates.xlsx', index=False)

"""
# folds

fold_list = []
# the fold dataframes in part-d (it was saved in excel format)
for i in range(1, 6):
    fold_list.append(pd.read_excel(f'Fold_{i}.xlsx'))

num_folds = 5
max_m = 8
k=9

column_headers = [f'm={m}' for m in range(2, max_m + 1)]
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
    m_range = range(2, max_m + 1)
    error_rate_list = np.zeros(len(m_range))
    for index, m in enumerate(m_range):
        predicted_labels = fuzzy_knn_classifier_ID2693653(training_dataset_data, training_dataset_true_labels, test_dataset_data, k, m)
        test_error = np.mean(predicted_labels != test_dataset_true_labels)
        error_rate_list[index] = test_error
    Error_Table_Df.iloc[i] = error_rate_list

best_m_per_fold = []

for row_index, row in Error_Table_Df.iterrows():    
    best_m = row.astype(float).idxmin()  
    best_m_per_fold.append(best_m)
Error_Table_Df['Best m'] = best_m_per_fold

Error_Table_Df.to_excel('Error_Table_Df_CA4_PartIa_ID2693653.xlsx', index=True)


for i in range(num_folds):
    plt.figure(figsize=(8, 5))  # Plots the error rates vs k for each fold
    plt.plot(list(range(2, max_m + 1)), list(Error_Table_Df.iloc[i, :-1]), marker='o', label=f'Fold {i + 1}')
    plt.plot(list(range(2, max_m + 1)), list(Error_Table_Df.iloc[i, :-1]), marker='o')
    plt.title(f'Error Rate vs m for Fold {i + 1}')
    plt.xlabel('m')
    plt.ylabel('Error Rate')
    plt.xticks(list(range(2, max_m + 1)))
    plt.grid()
    plt.show()

"""
# Part b-)
m=2
k_range = range(1, 11) 
modified_fuzzy_knn_error_rate_list = np.zeros(len(k_range))


for index, k in enumerate(k_range):
    predicted_labels = modified_fuzzy_knn_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data, k, m)
    test_error = np.mean(predicted_labels != test_split_true_labels)
    modified_fuzzy_knn_error_rate_list[index] = test_error


plt.plot(list(k_range), modified_fuzzy_knn_error_rate_list, label="Modified Fuzzy KNN Error Rate", marker='o', linestyle='-', color='red')
plt.title('Error Rate vs k')
plt.xlabel('k')
plt.ylabel('Error Rate')
plt.xticks(list(k_range))
plt.legend()
plt.grid()
plt.show()



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

for row_index, row in Error_Table_Df.iterrows():    
    best_k = row.astype(float).idxmin()  
    best_k_per_fold.append(best_k)
Error_Table_Df['Best k'] = best_k_per_fold

Error_Table_Df.to_excel('Error_Table_Df_PartIb_ID2693653.xlsx', index=True)


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

# Part c-)

# RNN with standard KNN


r_range = np.linspace(0.01, 3, 30)

rnn_error_rate_list = np.zeros(len(r_range))

for index, r in enumerate(r_range):
    predicted_labels = rnn_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data, r)
    test_error = np.mean(predicted_labels != test_split_true_labels)
    rnn_error_rate_list[index] = test_error

plt.plot(list(r_range), rnn_error_rate_list, label="RNN Error Rate", marker='o', linestyle='-', color='red')
plt.title('Error Rate vs r')
plt.xlabel('r')
plt.ylabel('Error Rate')
plt.xticks(list(r_range))
plt.legend()
plt.grid()
plt.show()

rnn_error_rates_df = pd.DataFrame({
    'r': r_range,
    'Error Rate': rnn_error_rate_list
})

rnn_error_rates_df.to_excel('RNN_Error_Rates.xlsx', index=False)

# Part d-)
# RNN with modified KNN


r_range = np.linspace(0.01, 3, 30)

m_rnn_error_rate_list = np.zeros(len(r_range))
m_rnn_error_rate_list_train = np.zeros(len(r_range))

for index, r in enumerate(r_range):
    predicted_labels = m_rnn_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data, r)
    predicted_labels_train = m_rnn_classifier_ID2693653(train_split_data, train_split_true_labels, train_split_data, r)
    test_error = np.mean(predicted_labels != test_split_true_labels)
    train_error = np.mean(predicted_labels_train != train_split_true_labels)
    m_rnn_error_rate_list[index] = test_error
    m_rnn_error_rate_list_train[index] = train_error

plt.plot(list(r_range), m_rnn_error_rate_list, label="MRNN Error Rate", marker='o', linestyle='-', color='blue')
plt.title('Error Rate vs r')
plt.xlabel('r')
plt.ylabel('Error Rate')
plt.xticks(list(r_range))
plt.legend()
plt.grid()
plt.show()

m_rnn_error_rates_df = pd.DataFrame({
    'r': r_range,
    'Error Rate': m_rnn_error_rate_list
})

m_rnn_error_rates_df.to_excel('MRNN_Error_Rates.xlsx', index=False)
m_rnn_error_rates_train_df = pd.DataFrame({
    'r': r_range,
    'Train Error Rate': m_rnn_error_rate_list_train
})

plt.plot(list(r_range), m_rnn_error_rate_list_train, label="MRNN Error Rate (Train)", marker='o', linestyle='-', color='green')
plt.title('Train Error Rate vs r')
plt.xlabel('r')
plt.ylabel('Train Error Rate')
plt.xticks(list(r_range))
plt.legend()
plt.grid()
plt.show()


m_rnn_error_rates_train_df.to_excel('MRNN_Train_Error_Rates.xlsx', index=False)