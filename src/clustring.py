import numpy as np


def random_centroids(pixels, k):
    # A 2D NumPy array of shape (k, 3), k is the number of clusters
    # and 3 represents the RGB color values of each centroid.
    centroids = pixels[np.random.choice(pixels.shape[0], k, replace=False)]
    return centroids


def assign_pixels_to_centroids(pixels, centroids):
    # assignments is a 1D array,
    # where each element is the index of the nearest centroid for the corresponding pixel.
    distances = np.linalg.norm(pixels[:, np.newaxis] - centroids, axis=2)
    assignments = np.argmin(distances, axis=1)
    return assignments


def update_centroids(pixels, assignments, k):
    # selects all pixels assigned to the i-th centroid.
    # then calculates the mean of the selected pixels along axis 0 (the RGB channels).
    # new_centroids is a 1D array of shape (3,) representing the new position of the i-th centroid.
    new_centroids = np.array([pixels[assignments == i].mean(axis=0) for i in range(k)])
    return new_centroids


def k_means(pixels, k, max_iters=20):
    centroids = random_centroids(pixels, k)

    for i in range(max_iters):
        assignments = assign_pixels_to_centroids(pixels, centroids)
        new_centroids = update_centroids(pixels, assignments, k)

        # Check for convergence
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return centroids, assignments
