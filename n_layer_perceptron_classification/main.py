import pandas as pd

from compare import compare
from analysis import analyse

if __name__ == '__main__':
    dataset = pd.read_csv("Iris.csv")

    compare(dataset)

    # analyse(dataset)
