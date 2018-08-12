import pandas as pd

ratings = pd.read_csv('../data/ratings.csv')
movies = pd.read_csv('../data/movies.csv')

min_ratings_count = 100
user_genres = ['Comedy', 'Romance']


movies_count = ratings.groupby('movieId').count().reset_index() #получаем количество фильмов с оценками
movies_with_n_ratings = movies_count[ movies_count['rating'] >= min_ratings_count] # фильтруем, берем только те у которых значение больше 100
list_of_movies_with_n_ratings = movies_with_n_ratings['movieId'].tolist() #переводим в список

ratings = ratings[ ratings['movieId'].isin(list_of_movies_with_n_ratings) ]# новый датафрейм с исключенными значениями

ratings = ratings.groupby('movieId').mean().reset_index()#подсчитываем средний рейтинг для каждого фильма (соответственно для всех колонок это работает)

joined = ratings.merge(movies, on = 'movieId', how = 'left')# join двух таблиц для получения жанров
# print(joined.head())
# print(joined.info())

def genre_matching(row):
    genres_ = row ['genres'].split('|')
    for genre in genres_:
        if genre in user_genres:
            return True
    return False

joined['type'] = joined.apply(genre_matching, axis=1)
joined = joined[joined['type']==True].sort_values(by='rating', ascending=False)
print(joined.head())
