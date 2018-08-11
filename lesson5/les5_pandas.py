import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('../data/ratings.csv')


data[ data['userId'] == 1 ]['rating'].value_counts()

table = data.pivot_table(index='userId', columns='rating', values='timestamp', aggfunc='count', fill_value=0, margins=True)


table = table.reset_index()#=>table.reset_index(inplace=True)

#удаляем пользователя с id All

table = table[ table['userId'] != 'All' ]

print(table.sort_values(5.0, ascending=False)[['userId',5.0]].head())

table.sort_values(5.0, ascending=False)[5.0].head().plot(kind='kde')
plt.show()
