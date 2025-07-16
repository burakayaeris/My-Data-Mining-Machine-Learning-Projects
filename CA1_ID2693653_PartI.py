# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np

titanic_data = pd.read_csv("Titanic-Dataset.csv")

# Question a: Drop some of the columns
titanic_data_modified = titanic_data.drop(columns=["PassengerId", "Name", "Ticket"])

print(titanic_data_modified.head())
print("\n")

# Question b: Sample size and number of attributes
sample_size = titanic_data_modified.shape[0]
print(f"Sample size: {sample_size}")
num_attributes = titanic_data_modified.shape[1]
print(f"Number of attributes: {num_attributes}")

# Question c: Missing values
missing_values = titanic_data_modified.isnull() 
print("\n")
print(missing_values) # it prints true if there is a missing value in the dataset
missing_values_count = missing_values.sum() # Count of missing values in each attribute
print(missing_values_count)
# Total number of missing values
print(f"Total number of missing values: {missing_values_count.sum()}")

# Question d
# data types of the attributes
#print(titanic_data_modified.dtypes) this line was printed for the first time, but it is not necessary to print it again

# Mean and standard deviation of the Age and Fare attributes

mean_age = titanic_data_modified["Age"].mean()
std_age = titanic_data_modified["Age"].std()
print("\n")
print(f"Mean Age: {mean_age:.2f}, Standard Deviation of Age: {std_age:.2f}")
print("\n")

mean_fare = titanic_data_modified["Fare"].mean()
std_fare = titanic_data_modified["Fare"].std()


print(f"Mean Fare: {mean_fare:.2f}, Standard Deviation of Fare: {std_fare:.2f}")
print("\n")

# Question e: Frequency of each nominal (categorical) attribute

# For 'Sex' attribute
print(titanic_data_modified["Sex"].value_counts())

print("\n")

# For 'Cabin' attribute
print(titanic_data_modified["Cabin"].value_counts())

print("\n")

# For 'Embarked' attribute
print(titanic_data_modified["Embarked"].value_counts())
