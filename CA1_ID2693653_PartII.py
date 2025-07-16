# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np

titanic_data = pd.read_csv("Titanic-Dataset.csv")

# Dropping the attributes that are not needed and also the categorical attributes
titanic_data_modified = titanic_data.drop(columns=["PassengerId", "Name", "Ticket", "Sex","Cabin", "Embarked"])

print("Titanic data with removed attributes:\n")
print(titanic_data_modified.head())

# total number of missing values
total_missing = titanic_data_modified.isnull().sum() # 177 values are missing in the Age column

# we need to look at the distribution of the Age column to see how we can fill the missing values
# plotting the distribution of the Age column
#import matplotlib.pyplot as plt
#import seaborn as sns
# plotting the distribution of the Age column
#plt.figure(figsize=(10, 6))
#sns.histplot(titanic_data_modified['Age'], bins=30, kde=True) # we have a right skewed distribution
#plt.title('Distribution of Age')
# After plotting the distribution, we can see that the Age column has a right-skewed distribution.
# For this reason, we can fill the distribution with the median value of the Age column
titanic_data_modified['Age'].fillna(titanic_data_modified['Age'].median(), inplace=True)

num_data_points = titanic_data_modified.shape[0]
num_attributes = titanic_data_modified.shape[1]

# Standardizing the data

std_titanic_data = (titanic_data_modified - titanic_data_modified.mean(axis=0)) / titanic_data_modified.std(axis=0)
print("\n")
print(std_titanic_data.head())
print("\n")

# Making the covariance matrix of the standardized data
cov_matrix = np.zeros((num_attributes, num_attributes))
for i in range(num_attributes):
    for j in range(num_attributes):
        # calculating covariance of attribute i and j using titanic_data_normalized and appending it to the covariance matrix
        attr_i_vector = std_titanic_data.iloc[:, i]
        attr_j_vector = std_titanic_data.iloc[:, j]

        mean_attr_i = np.mean(attr_i_vector)
        mean_attr_j = np.mean(attr_j_vector)

        cov_matrix[i][j] = np.sum((attr_i_vector - mean_attr_i) * (attr_j_vector - mean_attr_j)) / (len(attr_i_vector) - 1)

# Covariance matrix of normalized data
cov_matrix = pd.DataFrame(cov_matrix, columns=std_titanic_data.columns, index=std_titanic_data.columns)

print("\n")
print("Covariance matrix of standardized data:")
print(cov_matrix)
print("\n")

# Eigenvalues and eigenvectors of the covariance matrix
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix.values)

# Tranforming the data using the eigenvectors
titanic_data_transformed = np.dot(std_titanic_data, eigenvectors)

# print(titanic_data_transformed) # to test, i printed the transformed data, but it is not necessary to print it again

# Calculating variance of the transformed data
variance = np.var(titanic_data_transformed, axis=0)

# Sorting the variance in descending order
sorted_variance = np.sort(variance)[::-1]

# Sorting features by variance
sorted_indices = np.argsort(variance)[::-1]
sorted_indices

# Transformed data with sorted features
titanic_data_transformed_sorted = titanic_data_transformed[:, sorted_indices]

# Total variance of the data
total_variance = np.sum(variance)

# Choosing the "r" new attributes such that the variance of the new attributes is greater than 95% of the total variance
# As a result, all new attributes were used 
r = 0
cumulative_variance = 0
for i in range(num_attributes):
    cumulative_variance += sorted_variance[i]
    if cumulative_variance / total_variance >= 0.95:
        r = i + 1
        break

# Transformed data with "r" new attributes
titanic_data_transformed_sorted_r = titanic_data_transformed_sorted[:, :r]

# Cosine similarity between every pair of transformed data points
cosine_similarity_matrix = np.zeros((num_data_points, num_data_points))

for i in range(num_data_points):
    for j in range(num_data_points):
        numerator = np.sum(titanic_data_transformed_sorted_r[i,:] * np.transpose(titanic_data_transformed_sorted_r[j,:]))
        
        denominator = np.sqrt(np.sum(titanic_data_transformed_sorted_r[i,:] * np.transpose(titanic_data_transformed_sorted_r[i,:]))) * np.sqrt(np.sum(titanic_data_transformed_sorted_r[j,:] * np.transpose(titanic_data_transformed_sorted_r[j,:])))
        cosine_similarity_matrix[i][j] = numerator / denominator

count = 0
for i in range(num_data_points):
    for j in range(i + 1, num_data_points):
        print(f"Cosine similarity (After PCA algorithm) between point {i} and {j}: {cosine_similarity_matrix[i][j]:.6f}")
        count = count + 1
        if count == 10:
            break
    if count == 10:
        break

