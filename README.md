# Probably Interesting Data
*Gage Benne & Andy Monroe*

*EECS738*

## Introduction
For our project, we attempted to analyze two different datasets, both by using the k-means clustering strategy in order to flesh out a wholistic understanding of k-means, how it works, what it can do, and what it *can't* do.

The Iris dataset we used was very easy for applying k-means, as we could find a clean separation of one type of iris from the other two when comparing sepal width versus sepal length.

For the second dataset, we realized the shortcomings of the k-means clustering strategy. In particular, k-means just optimizes to get a roughly even amount of datapoints as close to k centers as possible. This is fine for a set of roughly evenly-sized clusters, but some datasets have clusters of very different sizes. With k-means, the algorithm typically shows bias towards the largest cluster for all centroids, instead of placing a centroid in the smaller cluster, which is what we really would desire.

By attempting to apply k-means to a nicely-clustered dataset, and a skew-clustered dataset, we have developed a profile of the k-means clustering strategy, warts and all. The following sections provide the details and visuals for each dataset.

## Dataset 1: Iris
Sepal Width vs. Sepal Length



## Dataset 2:

[Reference](https://mubaris.com/posts/kmeans-clustering/)
