import matplotlib.pyplot as plot
import seaborn as sns
from sklearn.datasets import load_iris


def analyse(dataset):
    iris = dataset.drop(columns='Id')
    sns.pairplot(data=iris, vars=('SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'), hue='Species')
    iris.hist(alpha=0.5, figsize=(20, 20), color='red')
    iris.plot(subplots=True, figsize=(10, 10), sharex=False, sharey=False)
    plot.show()

    iris = load_iris()
    plot.scatter(iris.data[:, 2], iris.data[:, 3], alpha=1, c=iris.target, edgecolors='black')
    plot.colorbar(ticks=([0, 1, 2]))
    plot.title('Petals')
    plot.xlabel('Petal length')
    plot.ylabel('Petal width')
    plot.show()

    plot.scatter(iris.data[:, 0], iris.data[:, 1], alpha=1, c=iris.target, edgecolors='black')
    plot.colorbar(ticks=([0, 1, 2]))
    plot.title('Sepals')
    plot.xlabel('Sepal length')
    plot.ylabel('Sepal width')
    plot.legend()
    plot.show()

    iris = dataset.drop(columns='Id')
    plot.figure(figsize=(15, 10))
    plot.subplot(2, 2, 1)
    sns.violinplot(x='Species', y='PetalLengthCm', data=iris)
    plot.subplot(2, 2, 2)
    sns.violinplot(x='Species', y='PetalWidthCm', data=iris)
    plot.subplot(2, 2, 3)
    sns.violinplot(x='Species', y='SepalLengthCm', data=iris)
    plot.subplot(2, 2, 4)
    sns.violinplot(x='Species', y='SepalWidthCm', data=iris)
    plot.show()

    plot.figure(figsize=(7, 4))
    sns.heatmap(iris.corr(), annot=True,
                cmap='cubehelix_r')  # draws  heatmap with input as the correlation matrix calculted by(iris.corr())
    plot.show()

    sns.FacetGrid(dataset, hue="Species", size=5).map(sns.distplot, "SepalWidthCm", hist_kws={"alpha": .2}).add_legend()
    plot.show()
