import os
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def kmeans(dataset, xlabel, ylabel, k):
    # Get dataset name without extension or path
    dataset_name = os.path.splitext(os.path.basename(dataset))[0]
    if not os.path.exists(dataset_name):
        os.makedirs(dataset_name)

    print("---K-means clustering---")
    print("Dataset: {}".format(dataset_name))
    print("X: {}".format(xlabel))
    print("Y: {}".format(ylabel))
    print("k: {}".format(k))

    # Get plotting up and going
    plt.rcParams['figure.figsize'] = (16, 9)
    plt.style.use('ggplot')

    # Importing the dataset
    data = pd.read_csv(dataset)
    print("Input data and shape:")
    print(data.shape)
    data.head()

    # Getting the values and plotting it
    f1 = data[xlabel].values
    f2 = data[ylabel].values
    X = np.array(list(zip(f1, f2)))
    plt.scatter(f1, f2, c='black', s=5)

    # X and Y coordinates of random starter centroids
    C_x = np.random.randint(np.min([i[0] for i in X]), np.max([i[0] for i in X]), size=k)
    C_y = np.random.randint(np.min([i[1] for i in X]), np.max([i[1] for i in X]), size=k)
    C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
    print("Initial Centroids:")
    print(C)

    # Add centroid to plot
    plt.scatter(C_x, C_y, marker='o', s=100, c='black')

    # Save initial plot
    plt.title("Initial: {}".format(dataset_name))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig("{}/{}_{}_initial.png".format(dataset_name, xlabel, ylabel))
    plt.close()

    # To store the value of centroids when it updates
    C_old = np.zeros(C.shape)
    # Clustering labels
    clusters = np.zeros(len(X))

    # Loop until distance between new centroids and old centroids is zero
    error = dist(C, C_old, None)
    while error != 0:
        # Assigning each value to closest cluster
        for i in range(len(X)):
            distances = dist(X[i], C)
            cluster = np.argmin(distances)
            clusters[i] = cluster
        # Storing old centroid values
        C_old = deepcopy(C)
        # Finding new centroids (average value)
        for i in range(k):
            points = [X[j] for j in range(len(X)) if clusters[j] == i]
            C[i] = np.mean(points, axis=0)
        error = dist(C, C_old, None)

    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    fig, ax = plt.subplots()
    for i in range(k):
            points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
            ax.scatter(points[:, 0], points[:, 1], s=5, c=colors[i])
    ax.scatter(C[:, 0], C[:, 1], marker='*', s=100, c='black')

    # Save clustering plot
    plt.title("Clustering: {}".format(dataset_name))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig("{}/{}_{}_clustering.png".format(dataset_name, xlabel, ylabel))
    plt.close()

# Euclidean distance calculator
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)
