import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def analysis(csvname):
    df = pd.read_csv(csvname)
    df.drop("id", axis=1)
    df['date'] = df['date'].str.replace("T000000", "")
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df["date"].dt.year
    df['month'] = df["date"].dt.month
    df["day"] = df["date"].dt.day

    df = df.drop("date", axis=1)
    df.info()
    print(df.isnull().sum())

    plt.figure(figsize=(20, 15))

    columns2 = ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'sqft_basement', 'view',
                'zipcode', 'lat', 'long', 'floors', 'yr_built', 'grade']
    sns.heatmap(df[columns2].corr(), annot=True, cmap=plt.cm.Reds)
    sorted_cor = df[columns2].corr()["price"].sort_values(ascending=False)
    print(sorted_cor)
    df.corr()["price"].sort_values(ascending=False)

    df.hist(bins=25, figsize=(16, 16), xlabelsize='10', ylabelsize='10', xrot=-15)
    plt.show()
