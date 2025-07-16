# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from partition_dataset_ID2693653 import *
from knn_classifier_ID2693653 import *

winconsin_df = pd.read_excel('Wisconsin Diagnostic Breast Cancer.xlsx')

# min-max normalization
winconsin_df_normal = (winconsin_df - winconsin_df.min()) / (winconsin_df.max() - winconsin_df.min())

train_split, test_split = partition_dataset_ID2693653(winconsin_df_normal)

train_split_data = train_split.iloc[:,:-1]
train_split_true_labels = train_split.iloc[:,-1]

test_split_data = test_split.iloc[:,:-1]
test_split_true_labels = test_split.iloc[:,-1]


k_range = range(1, 11)
error_rate_list = np.zeros(len(k_range))

for index, k in enumerate(k_range):
    predicted_labels = knn_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data, k)
    test_error = np.mean(predicted_labels != test_split_true_labels)
    error_rate_list[index] = test_error

plt.plot(list(k_range), error_rate_list, marker='o')
plt.title('Error Rate vs k')
plt.xlabel('k')
plt.ylabel('Error Rate')
plt.xticks(list(k_range))
plt.grid()
plt.show()