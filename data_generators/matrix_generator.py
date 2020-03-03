from random import randint
import pandas as pd


def rand_arr(minmax, size):
    return [randint(-minmax, minmax) for _ in range(size)]


def rand_matrix(rows, columns, minmax):
    return [rand_arr(minmax, columns) for _ in range(rows)]


matrix = rand_matrix(5, 5, 5)

df = pd.DataFrame(matrix)

df2 = pd.concat([df, df])

df2.reset_index()

df4 = pd.concat([df2, df2], axis=1)

df4.reset_index(inplace=True)

df4.columns = [i for i in range(len(df4.columns))]

df4.rolling(5, min_periods=2).mean()