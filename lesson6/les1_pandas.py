import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
data = pd.read_csv('../data/ratings.csv')
movies = pd.read_csv('../data/movies.csv')

comedy = movies[movies['genres'].str.contains('Comedy')]
# print(comedy.head())

dataList = [
    { 'date': '2017-07-01', 'value': 100 },
    { 'date': '2017-07-02', 'value': 200 },
    { 'date': '2017-07-03', 'value': 300 },
    { 'date': '2017-07-04', 'value': 400 },
    { 'date': None, 'value': 500 },
]
df = pd.DataFrame(dataList)
#ЕСЛИ В СТОЛОБЦЕ ХОТЯ ОДНО ЗНАЧЕНИЕ РАВНО NONE - ЭТО ПРИВОДИТ К ОШИБКИ МЕТОДА, ЧТОБЫ ЭТОГО ИЗБЕЖАТЬ ИСПОЛЬЗУЕМ ИМЕНОВАНЫЙ ПАРАМЕТР na=False
# print(df[df['date'].str.contains('04', na = False)])


comedy = movies[(movies['genres'].str.contains('Comedy'))|(movies['genres'].str.contains('Fantasy'))]
# print(comedy)

#параметр expand = True, который запишет каждый элемент получившегося листа в отдельный столбец
years_df = movies['title'].str.split('(', expand=True)

# print(years_df[~years_df[4].isnull()])

# print(movies[1874:1875].title)

# print(movies[1874:1875].iloc[0,1])

production_year = years_df[1].str.replace(')', '')

series = production_year

# print(production_year)
# pprint(production_year.to_frame(name='x').query('x == "1996" ').count())#!!!
# print(series[series == '1996'].count())#!!!!!!
# print(series.loc[lambda x: x =='1996'].count())#!!!!
# print(series.where(lambda x: x == '1996').count())#!!!
# print(series.compress(lambda x: x == '1996').count())#!

# mask = series.values == '1996'
# print(pd.Series(series.values[mask], series.index[mask]))#!!!???!!!

print(series.str.count('1996')==1)
