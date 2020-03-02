from random import randint
import pandas as pd


def rand_arr(minmax, size):
    return [randint(-minmax, minmax) for _ in range(size)]


def rand_matrix(rows, columns, minmax):
    return [rand_arr(minmax, columns) for _ in range(rows)]


matrix = rand_matrix(5, 5, 5)

df = pd.DataFrame(matrix)
