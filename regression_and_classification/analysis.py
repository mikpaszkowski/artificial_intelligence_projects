import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
import seaborn as sns
from metrics import metrics


def analysis(csvname):
    df = pd.read_csv(csvname)
    df = df.drop(["id"], axis=1)
    # converting one non-numeric date column to three numeric columns: year, month, day
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df = df.drop("date", axis=1)
    # df = df.sort_values(['price'], ascending=False).iloc[980:]
    sns.distplot(df['price'])

    df.info()
    print(df.isnull().sum())

    cor = df.corr()
    plt.figure(figsize=(20, 15))
    columns = ['price','bedrooms','bathrooms','sqft_living', 'sqft_lot', 'waterfront', 'view', 'sqft_basement', 'zipcode', 'lat', 'long', 'year', 'month', 'day', 'floors','grade','yr_built','condition']
    columns2 = ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'sqft_basement', 'view',
               'zipcode', 'lat', 'long','floors', 'yr_built', 'grade']
    sns.heatmap(df[columns2].corr(), annot=True, cmap=plt.cm.Reds)
    sorted_cor = df[columns2].corr()["price"].sort_values(ascending=False)
    print(sorted_cor)
    df.corr()["price"].sort_values(ascending=False)


    df.hist(bins=25,figsize=(16,16),xlabelsize='10',ylabelsize='10',xrot=-15)
    plt.show()
