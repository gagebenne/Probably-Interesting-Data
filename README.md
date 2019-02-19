# Probably Interesting Data
*Gage Benne & Andy Monroe*

*EECS738*

## Introduction
For our project, we attempted to analyze two different datasets, both by using the k-means clustering strategy in order to flesh out a wholistic understanding of k-means, how it works, and what it can demonstrate.

The Iris dataset we used was very easy for applying k-means, as we could find a clean separation of one type of iris from the other two when comparing sepal width versus sepal length. This is a very standard dataset for demonstrating clustering of data, and our k-means implementation performed quite admirably in locating proper centroids for the two clusters.

The second dataset we used was census data plotting age versus capital gains. We were also able to effectively apply k-means here, however instead of demonstrating a particular relationship between age and capital gains, k-means demonstrates a clump of indivduals who reported exceptionally high capital gains. This group likely reached the maximum allowed by the census, which is how their cluster ended up being so close together.

By attempting to apply k-means to a nicely-clustered dataset, and a skew-clustered dataset, we have developed a profile of the k-means clustering strategy. The following sections provide the details and visuals for each dataset.

## Dataset 1: Iris
Sepal Width vs. Sepal Length

![Initial](iris/SepalLengthCm_PetalLengthCm_initial.png)
![Initial](iris/SepalLengthCm_PetalLengthCm_clustering.png)




## Dataset 2:

[Reference](https://mubaris.com/posts/kmeans-clustering/)
