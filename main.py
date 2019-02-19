from cluster import kmeans

dataset = "datasets/iris.csv"
xs = "SepalLengthCm"
ys = "PetalLengthCm"
k = 2
kmeans(dataset, xs, ys, k)

dataset = "datasets/adult.csv"
xs = "age"
ys = "capitalgain"
k = 2
kmeans(dataset, xs, ys, k)
