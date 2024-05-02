import numpy as np

class KMeans:
    def __init__(self, k=3, max_iter=100):
        self.k = k
        self.max_iter = max_iter

    def fit(self, X):
        # Initialize centroids randomly
        centroids_idx = np.random.choice(X.shape[0], self.k, replace=False)
        self.centroids = X[centroids_idx]

        for _ in range(self.max_iter):
            # Assign each data point to the closest centroid
            distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
            labels = np.argmin(distances, axis=0)

            # Update centroids based on the mean of data points assigned to each cluster
            new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])

            # Check for convergence
            if np.allclose(self.centroids, new_centroids):
                break

            self.centroids = new_centroids

        return labels

# Test the implementation with the given data objects
data_objects = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]])
kmeans = KMeans(k=3)
labels = kmeans.fit(data_objects)
print("Cluster Labels for Data Objects:")
for i, label in enumerate(labels):
    print(f"Data Object {i+1}: Cluster {label+1}")


import pandas as pd

# Load the IRIS dataset
iris_df = pd.read_csv("IRIS.csv")

# Remove the 'Species' column
iris_data = iris_df.drop(columns=['Species'])

# Convert dataframe to numpy array
iris_data_array = iris_data.values


import pandas as pd

# Load the IRIS dataset
iris_df = pd.read_csv("Iris.csv")

# Remove the 'Species' column
iris_data = iris_df.drop(columns=['Species'])

# Convert dataframe to numpy array
iris_data_array = iris_data.values


# Apply the developed k-Means clustering algorithm to the IRIS dataset
kmeans_iris = KMeans(k=3)
labels_iris = kmeans_iris.fit(iris_data_array)

# Display cluster labels for the IRIS dataset
print("\nCluster Labels for IRIS Dataset:")
for i, label in enumerate(labels_iris):
    print(f"Data Point {i+1}: Cluster {label+1}")
