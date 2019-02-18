from cluster import kmeans

print("K-means clustering")
dataset = "datasets/Iris.csv"
xs = "SepalLengthCm"
ys = "PetalLengthCm"
k = 2

kmeans(dataset, xs, ys, k)
