import matplotlib.pyplot as plot
import seaborn as sns
from sklearn.datasets import load_iris


def analyse(dataset):
    print(dataset.head(5))
    sns.pairplot(data=dataset, vars=('SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'), hue='Species')
    dataset.hist(alpha=0.5, figsize=(20, 20), color='red')
    dataset.plot(subplots=True, figsize=(10, 10), sharex=False, sharey=False)

    iris = load_iris()
    plot.scatter(iris.data[:, 2], iris.data[:, 3], alpha=1, c=iris.target, edgecolors='black')
    plot.colorbar(ticks=([0, 1, 2]))
    plot.title('Petals')
    plot.xlabel('Petal length')
    plot.ylabel('Petal width')

    plot.scatter(iris.data[:, 0], iris.data[:, 1], alpha=1, c=iris.target, edgecolors='black')
    plot.colorbar(ticks=([0, 1, 2]))
    plot.title('Sepals')
    plot.xlabel('Sepal length')
    plot.ylabel('Sepal width')
    plot.show()
