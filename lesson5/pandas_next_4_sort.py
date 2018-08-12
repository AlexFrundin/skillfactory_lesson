import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/ratings.csv')
#считаем сколько раз фильм встречался, соответственно идет подсчет и для остальных значений в сете -
#так мы группировали по movieId то только это значение остается не изменным
movies_count = data.groupby('movieId').count().reset_index()
#выбираем только те у которых один раз ставили оценку
movies_with_one_rating = movies_count[movies_count['rating']==1]

list_movies_one = movies_with_one_rating['movieId'].tolist()


data_clean = data[~data['movieId'].isin(list_movies_one)]

df = data_clean.groupby('movieId').mean().reset_index().sort_values(by='rating', ascending=False)

print(data_clean[(data['movieId']==6958)|(data['movieId']==99764)|(data['movieId']==309)])
