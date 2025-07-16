# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np

def naive_bayes_classifier_ID2693653(train_split_data, train_split_true_labels, test_split_data):

    unique_labels, label_counts = np.unique(train_split_true_labels, return_counts=True)
    class_probability_distribution = pd.Series(label_counts / len(train_split_true_labels), index=unique_labels)
    total_number_of_classes = len(unique_labels)
    number_of_features = train_split_data.shape[1]
    feature_categories = []
    feature_category_counts = []
    for feature_name in train_split_data.columns:
        unique_values = train_split_data[feature_name].unique()
        feature_categories.append(unique_values)
        feature_category_counts.append(len(unique_values))
    maximum_categories = max(feature_category_counts)

    feature_class_conditional_probabilities = np.full((number_of_features, maximum_categories, total_number_of_classes),0.000001)
    for feature_index, feature_name in enumerate(train_split_data.columns):
        current_categories = feature_categories[feature_index]
        for category_index, category_value in enumerate(current_categories):
            for class_index, class_label in enumerate(unique_labels):
                feature_class_mask = (train_split_data[feature_name] == category_value) & (train_split_true_labels == class_label)
                feature_class_count = np.sum(feature_class_mask)
                class_count = np.sum(train_split_true_labels == class_label)
                if class_count > 0:
                    feature_class_conditional_probabilities[feature_index, category_index, class_index] = (feature_class_count / class_count)

    test_predicted_labels = np.zeros(len(test_split_data), dtype=unique_labels.dtype)
    for instance_index, (_, test_instance) in enumerate(test_split_data.iterrows()):
        instance_class_probabilities = np.array([class_probability_distribution[label] for label in unique_labels]) 
        for feature_index, feature_name in enumerate(test_split_data.columns):
            feature_value = test_instance[feature_name]
            current_categories = feature_categories[feature_index]
            
            if feature_value in current_categories:
                if isinstance(current_categories, np.ndarray):
                    category_index = np.where(current_categories == feature_value)[0][0]
                else:
                    category_index = list(current_categories).index(feature_value)
                for class_index in range(total_number_of_classes):
                    instance_class_probabilities[class_index] *= (feature_class_conditional_probabilities[feature_index, category_index, class_index])
            else:
                instance_class_probabilities *= 0.000001
        test_predicted_labels[instance_index] = unique_labels[np.argmax(instance_class_probabilities)]
    return test_predicted_labels

