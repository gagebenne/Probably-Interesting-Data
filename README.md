# Probably Interesting Data
*Gage Benne & Andy Monroe*

*EECS 738*

## Introduction
For our project, we attempted to analyze two different datasets, both by using the k-means clustering strategy in order to flesh out a wholistic understanding of k-means, how it works, and what it can demonstrate. We targeted relatively continuous datasets as much as possible, as clustering is typically more interesting on continuous-axis datapoints instead of highly-discrete datapoints represented in some of the datasets we examined.

The Iris dataset we used was very easy for applying k-means, as we could find a clean separation of one type of iris from the other two when comparing sepal width versus sepal length. This is a very standard dataset for demonstrating clustering of data, and our k-means implementation performed quite admirably in locating proper centroids for the two clusters.

The second dataset we used was census data plotting age versus capital gains. We were also able to effectively apply k-means here, however instead of demonstrating a particular relationship between age and capital gains, k-means demonstrates a clump of indivduals who reported exceptionally high capital gains. This group likely reached the maximum allowed by the census, which is how their cluster ended up being so close together.

By attempting to apply k-means to a nicely-clustered dataset, and a skew-clustered dataset, we have developed a profile of the k-means clustering strategy. The following sections provide the details and visuals for each dataset.

## Process
We opted to implement our k-means clustering strategy in Python so that we may utilize its many plotting and scientific computing packages, along with pandas.  We love pandas.  In getting started, we followed key points on a guide from [Mubaris NK](https://mubaris.com/posts/kmeans-clustering/).

The `kmeans` function takes a dataset, two columns to consider in the calculations, as well as the k-value.  Initially the basic dataset is plotted and saved as a comparison to the later clustered data.

Next, k number of initial centroids are found as a random X and Y value within the domain and range respectively.


```python
C_x = np.random.randint(np.min([i[0] for i in X]), np.max([i[0] for i in X]), size=k)
C_y = np.random.randint(np.min([i[1] for i in X]), np.max([i[1] for i in X]), size=k)
```


After that, the program begins to cluster by assigning each point to the closest centroid (cluster).  After, the centroids are repositioned based on the average value of the points.  This process loops until the distance between the newly calculated centroids and old centroids is zero.

```python
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
```

After all is said and done, the clusters are represented visually by assigning colors to points and marking final centroids.  All files are saved using some lovely os path grabbing.

## Dataset 1: Iris
### Basic Idea
This is a very common example dataset for exemplifying k-means clustering, and we thought we would start off by making sure we could properly replicate the results of others. We compared sepal width versus sepal length for three species of iris plants, which, as it turns out, have two distinct width/ratios that are observable both to the human eye, and also to the k-means algorithm. The cluster to the left is the anomoly species, at least as opposed to the other two species which lie in the other cluster.

Sepal Width vs. Sepal Length

![Initial](iris/SepalLengthCm_PetalLengthCm_initial.png)

![Initial](iris/SepalLengthCm_PetalLengthCm_clustering.png)


## Dataset 2:
### Basic Idea
We thought it would be interesting to poke around in census data for our next statistical analysis. We initially had selected age versus capital gains, because we thought maybe there would be notable changes after a certain point in age, but what we ended up finding was a population of people of various ages that recorded substantially greater capital gains than the vast majority of the population. We were interested in trying out k-means to see how well it would capture a set of fewer datapoints that ended in a more one-dimensional cluster. As you can view yourself in the charts below, our k-means algorithm performed just as well the second time, and successfully separted the two clusters shown.

![Initial](adult/age_capitalgain_initial.png)

![Initial](adult/age_capitalgain_clustering.png)


# K-Means Reference
[Reference](https://mubaris.com/posts/kmeans-clustering/)
