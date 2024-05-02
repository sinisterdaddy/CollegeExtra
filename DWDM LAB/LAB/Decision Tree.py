# import pandas as pd
# import numpy as np

# # Function to calculate entropy
# def entropy(labels):
#     """Calculate the entropy of a list of labels."""
#     unique_labels, counts = np.unique(labels, return_counts=True)
#     probabilities = counts / len(labels)
#     entropy_value = -np.sum(probabilities * np.log2(probabilities))
#     return entropy_value

# # Function to calculate information gain
# def information_gain(data, split_attribute_name, target_name):
#     """Calculate the information gain for a given split attribute."""
#     total_entropy = entropy(data[target_name])
#     values, counts = np.unique(data[split_attribute_name], return_counts=True)
#     weighted_entropy = np.sum([(counts[i] / np.sum(counts)) *
#                                entropy(data.where(data[split_attribute_name] == values[i]).dropna()
#                                        [target_name])
#                                for i in range(len(values))])
#     information_gain_value = total_entropy - weighted_entropy
#     return information_gain_value

# # Function to calculate Gini index
# def gini_index(labels):
#     """Calculate the Gini index of a list of labels."""
#     unique_labels, counts = np.unique(labels, return_counts=True)
#     probabilities = counts / len(labels)
#     gini_index_value = 1 - np.sum(probabilities**2)
#     return gini_index_value

# # Function to find the best splitting criterion
# def find_best_split(data, target_name, measure):
#     """Find the best splitting criterion based on the specified measure."""
#     best_measure_value = 0
#     best_split_attribute = None
#     partitions = None
#     for column in data.columns[:-1]:
#         if measure == 'Information Gain':
#             current_measure_value = information_gain(data, column, target_name)
#         elif measure == 'Gini Index':
#             current_measure_value = gini_index(data[column])
#         if current_measure_value > best_measure_value:
#             best_measure_value = current_measure_value
#             best_split_attribute = column
#         if measure == 'Information Gain':
#             partitions = {value: data[data[best_split_attribute] == value] for value in
#                           data[best_split_attribute].unique()}
#         elif measure == 'Gini Index':
#             partitions = {value: data[data[best_split_attribute] == value] for value in
#                           np.unique(data[best_split_attribute])}
#     return best_split_attribute, partitions, best_measure_value

# # Load the iris dataset
# iris_data = pd.read_csv('iris.csv')

# # Example usage with iris.csv
# print("Information Gain:")
# split_criteria, data_partitions, measure_value = find_best_split(iris_data, 'Species', 'Information Gain')
# print("Best Splitting Criterion:", split_criteria)
# print("Data Partitions after Splitting:")
# for value, partition in data_partitions.items():
#     print("Partition for {}: \n{}".format(value, partition))
# print("Information Gain Value:", measure_value)
# print("\nGini Index:")
# split_criteria, data_partitions, measure_value = find_best_split(iris_data, 'Species', 'Gini Index')
# print("Best Splitting Criterion:", split_criteria)
# print("Data Partitions after Splitting:")
# for value, partition in data_partitions.items():
#     print("Partition for {}: \n{}".format(value, partition))
# print("Gini Index Value:", measure_value)





import pandas as pd
import numpy as np

# Function to calculate entropy
def entropy(labels):
    """Calculate the entropy of a list of labels."""
    unique_labels, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    entropy_value = -np.sum(probabilities * np.log2(probabilities))
    return entropy_value

# Function to calculate information gain
def information_gain(data, split_attribute_name, target_name):
    """Calculate the information gain for a given split attribute."""
    total_entropy = entropy(data[target_name])
    values, counts = np.unique(data[split_attribute_name], return_counts=True)
    weighted_entropy = np.sum([(counts[i] / np.sum(counts)) *
                               entropy(data.where(data[split_attribute_name] == values[i]).dropna()
                                       [target_name])
                               for i in range(len(values))])
    information_gain_value = total_entropy - weighted_entropy
    return information_gain_value

# Function to calculate Gini index
def gini_index(labels):
    """Calculate the Gini index of a list of labels."""
    unique_labels, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    gini_index_value = 1 - np.sum(probabilities**2)
    return gini_index_value

# Function to find the best splitting criterion
def find_best_split(data, target_name, measure):
    """Find the best splitting criterion based on the specified measure."""
    best_measure_value = 0
    best_split_attribute = None
    partitions = None
    for column in data.columns[:-1]:
        if measure == 'Information Gain':
            current_measure_value = information_gain(data, column, target_name)
        elif measure == 'Gini Index':
            current_measure_value = gini_index(data[column])
        if current_measure_value > best_measure_value:
            best_measure_value = current_measure_value
            best_split_attribute = column
        if measure == 'Information Gain':
            partitions = {value: data[data[best_split_attribute] == value] for value in
                          data[best_split_attribute].unique()}
        elif measure == 'Gini Index':
            partitions = {value: data[data[best_split_attribute] == value] for value in
                          np.unique(data[best_split_attribute])}
    return best_split_attribute, partitions, best_measure_value

# Load the tennis dataset
tennis_data = pd.DataFrame({
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Play Tennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
})

# Example usage with tennis.csv
print("Information Gain:")
split_criteria, data_partitions, measure_value = find_best_split(tennis_data, 'Play Tennis', 'Information Gain')
print("Best Splitting Criterion:", split_criteria)
print("Data Partitions after Splitting:")
for value, partition in data_partitions.items():
    print("Partition for {}: \n{}".format(value, partition))
print("Information Gain Value:", measure_value)
print("\nGini Index:")
split_criteria, data_partitions, measure_value = find_best_split(tennis_data, 'Play Tennis', 'Gini Index')
print("Best Splitting Criterion:", split_criteria)
print("Data Partitions after Splitting:")
for value, partition in data_partitions.items():
    print("Partition for {}: \n{}".format(value, partition))
print("Gini Index Value:", measure_value)
