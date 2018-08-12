import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

data = pd.read_csv('../data/ratings.csv')

movies = pd.read_csv('../data/movies.csv')


joined = data.merge(movies, how='left', on='movieId')
joined_right = data.merge(movies, how='right', on='movieId')
print(joined.info())
print(joined_right.info())
