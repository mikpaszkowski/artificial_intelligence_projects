import matplotlib.pyplot as plot
import seaborn as sns


def analyse(dataset):
    iris = dataset.drop(columns='Id')
    print(iris.head())
    #
    sns.pairplot(data=iris, vars=('SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'), hue='Species')
    iris.hist(alpha=0.5, figsize=(20, 20), color='red')
    iris.plot(subplots=True, figsize=(10, 10), sharex=False, sharey=False)
    plot.show()

    sns.scatterplot(iris['SepalLengthCm'], iris['SepalWidthCm'], alpha=1, hue=iris['Species'], s=50)
    plot.title('Comparison between various species based on petal length and width')
    plot.xlabel('Petal length')
    plot.ylabel('Petal width')
    plot.show()

    sns.scatterplot(iris['PetalLengthCm'], iris['PetalWidthCm'], alpha=1, hue=iris['Species'], s=50)
    plot.title('Comparison between various species based on sepal length and width')
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
    #
    # #heatmap
    plot.figure(figsize=(7, 4))
    plot.title('Correlation matrix')
    sns.heatmap(iris.corr(), annot=True, cmap='cubehelix_r')
    plot.show()

    # proability density function of PetalLength
    sns.set_style("whitegrid")
    sns.FacetGrid(dataset, hue="Species", size=6).map(sns.distplot, "PetalLengthCm").add_legend()
    sns.FacetGrid(dataset, hue="Species", size=6).map(sns.distplot, "PetalWidthCm").add_legend()
    sns.FacetGrid(dataset, hue="Species", size=6).map(sns.distplot, "SepalLengthCm").add_legend()
    sns.FacetGrid(dataset, hue="Species", size=6).map(sns.distplot, "SepalWidthCm").add_legend()
    plot.show()

    print(dataset.drop(columns="Id").describe())
