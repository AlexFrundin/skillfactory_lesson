import pandas as pd

ratings = pd.read_csv('../data/ratings_example.txt', sep = '\t')
# print(ratings.head())

movies = pd.read_csv('../data/movies_example.txt', sep = '\t')
# print(movies.head())


movies.drop_duplicates(subset = 'movieId', keep = 'first', inplace = True)
print(movies.head())

print(ratings.merge(movies, how = 'left', on = 'movieId'))
