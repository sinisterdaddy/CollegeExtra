import numpy as np

def euclidean_distance(P1, P2):
    return np.sqrt(np.sum((P1 - P2) ** 2))

# Example usage:
P1 = np.array([1, 2, 3])
P2 = np.array([4, 5, 6])
print(f"Euclidean Distance: {euclidean_distance(P1, P2)}")


def manhattan_distance(P1, P2):
    return np.sum(np.abs(P1 - P2))

# Example usage:
print(f"Manhattan Distance: {manhattan_distance(P1, P2)}")


def minkowski_distance(P1, P2, p=2):
    return np.power(np.sum(np.abs(P1 - P2) ** p), 1 / p)

# Example usage:
print(f"Minkowski Distance (p=2): {minkowski_distance(P1, P2, p=2)}")
print(f"Minkowski Distance (p=1): {minkowski_distance(P1, P2, p=1)}")


def cosine_similarity(A, B):
    dot_product = np.dot(A, B)
    norm_A = np.linalg.norm(A)
    norm_B = np.linalg.norm(B)
    return dot_product / (norm_A * norm_B)

# Example usage:
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
print(f"Cosine Similarity: {cosine_similarity(A, B)}")


def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

# Example usage:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Jaccard Similarity: {jaccard_similarity(set1, set2)}")


import pandas as pd
from scipy.stats import pearsonr

# Load the dataset (assuming it has columns