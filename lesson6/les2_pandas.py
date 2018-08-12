import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

data = pd.read_csv('../data/ratings.csv')

movies = pd.read_csv('../data/movies.csv')

# data['rating_10'] = data['rating']*2

# print(data.describe()) #вывод статической информации
# print(data.info())

# data['type'] = data['rating'].apply(lambda x: 'low' if x <= 2 else ( 'medium' if x <= 3.5 else ('high' if x <= 4.5 else 'best')))
# print(data.head())
# print(data['type'].value_counts())


user_genres = ['Adventure', 'Romance']

def genres_matching(row):
    genres_list_from_row = row['genres'].split('|')
    for genre in genres_list_from_row:
        if genre in user_genres:
            return True
    return False

# movies['user_match'] = movies.apply(genres_matching, axis=1)
def genres_count(row):
    return len(row['genres'].split('|'))

movies['count'] = movies.apply(genres_count, axis=1)
print(movies.describe())
