from sklearn.cluster import KMeans
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics

def main():
    iris = datasets.load_iris()

    x_iris = iris.data
    y_iris = iris.target

    x = pd.DataFrame(iris.data,columns=["Sepal Length","Sepal Width","Petal Length","Petal Width"])
    y = pd.DataFrame(iris.target,columns=["target"])
    print(x.head(5))

    print(x.shape)

    plt.scatter(x["Petal Length"],x["Petal Width"],c="blue")
    plt.xlabel("Petal Length")
    plt.ylabel("Petal Width")
    plt.show()

    model = KMeans(n_clusters=3,max_iter=1000)
    model.fit(x)
    y_label = model.labels_

    y_kmeans = model.predict(x)
    print(y_kmeans)

    acc=metrics.adjusted_rand_score(y_iris,y_kmeans)
    print(acc)

    plt.scatter(x["Petal Length"],x["Petal Width"],c=y_kmeans)
    plt.xlabel("Petal Length")
    plt.ylabel("Petal Width")
    plt.show()


if __name__ == "__main__":
    main()

