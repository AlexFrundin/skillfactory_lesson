import pandas as pd
import matplotlib.pyplot as plt
from pandas_show_plot import histogram


data = pd.read_csv('../data/ratings.csv')
#
# print((data['movieId'].unique()))
# print((data['movieId'].value_counts()))#->type pandas.core.series.Series


#Для рисование дата-сериес просто вызвать метод рисования, как только использован метод плот!!!! МАГИЯ
"""s = data['movieId'].value_counts().head(20).plot(kind='bar')
plt.show()"""

movieId_average = data.groupby('movieId').mean()

# print(movieId_average.head())

movieId_average = movieId_average.reset_index()

# print(movieId_average.head())

# print(movieId_average.sort_values(by = 'rating', ascending=False).head()) #сортировка по 'rating', если по нескольким нужна параметры передаем в виде списка ['rating', 'movieId']


#выборка

print(data[data['movieId']==71180])
