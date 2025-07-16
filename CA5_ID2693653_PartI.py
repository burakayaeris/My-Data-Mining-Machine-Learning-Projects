# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bin_ID2693653 import bin_ID2693653
from partition_dataset_ID2693653 import partition_dataset_ID2693653
from naive_bayes_classifier_ID2693653 import naive_bayes_classifier_ID2693653

winconsin_df = pd.read_excel('Wisconsin Diagnostic Breast Cancer.xlsx')

for column in winconsin_df.columns[:-1]:
    plt.figure(), plt.title(column),plt.xlabel(column), plt.ylabel('Frequency')
    winconsin_df[column].hist(grid=False, bins=18, color='red',edgecolor='black')
    stats = {'Skewness value': winconsin_df[column].skew(),'Mean': winconsin_df[column].mean(),'STD': winconsin_df[column].std()}
    x_pos, y_pos = 0.90, 0.90
    text_style = {'va': 'top','ha': 'right','fontsize': 12}
    box_style = {'facecolor': 'white','alpha': 0.5}
    plt.text(
            x_pos, y_pos,
            '\n'.join(f'{k}: {v:.2f}' for k, v in stats.items()),
            transform=plt.gca().transAxes,
            **text_style,
            bbox=box_style
        )
    plt.gca().patch.set_facecolor('lightgrey')
    plt.show()

error_rates = [] # in part b-)
for i in range(2,5):
    data_binned = bin_ID2693653(winconsin_df, i, 1)
    train_split, test_split = partition_dataset_ID2693653(data_binned)
    train_split_data = train_split.iloc[:,:-1]
    train_split_true_labels = train_split.iloc[:,-1]
    test_split_data = test_split.iloc[:,:-1]
    test_split_true_labels = test_split.iloc[:,-1]
    test_predictions = naive_bayes_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data)
    error_rate = np.mean(test_predictions != test_split_true_labels)
    error_rates.append(error_rate)
print(error_rates)

# naive rule error rate (part c) for benchmarking
values, counts = np.unique(train_split_true_labels, return_counts=True)
mojority_label = values[np.argmax(counts)]
naive_rule_test_predictions = [mojority_label] * len(test_split_data)
naive_rule_error_rate = np.mean(naive_rule_test_predictions != test_split_true_labels)
print(naive_rule_error_rate)
