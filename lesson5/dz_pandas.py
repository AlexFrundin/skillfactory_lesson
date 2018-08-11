import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('../data/ratings.csv')

userLifetime = data.groupby('userId').agg([min, max]).reset_index()

userLifetime['diff']=userLifetime['timestamp']['max']-userLifetime['timestamp']['min']

user_hunder = data.groupby('userId').count().reset_index()

user_hunder = user_hunder[user_hunder['movieId']>=100]['userId'].tolist()

life_time_user_hunder = userLifetime[userLifetime['userId'].isin(user_hunder)]

print((life_time_user_hunder['diff'].mean())/3600/24)
