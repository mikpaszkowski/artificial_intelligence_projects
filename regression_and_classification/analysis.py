import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score

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
    # df = df.sort_values(['price'], ascending=False).iloc[216:]
    # sns.distplot(df['price'])

    df.info()
    print(df.isnull().sum())

    cor = df.corr()
    plt.figure(figsize=(20, 15))
    # sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
    sorted_cor = df.corr()["price"].sort_values(ascending=False)
    print(sorted_cor)
    df.corr()["price"].sort_values(ascending=False)

    # df.hist()
    # plt.show()

    x = df.iloc[:, 1:]
    y = df.iloc[:, 0:1]
    X = x.values
    Y = y.values

    log_reg = LogisticRegression(solver='lbfgs', max_iter=400)
    log_reg.fit(X, Y.ravel())

    print(f'R² score: {r2_score(Y, log_reg.predict(X)) * 100}')
    print(f'score: {log_reg.score(X, y)}')
    metrics(log_reg, Y, log_reg.predict(X))
