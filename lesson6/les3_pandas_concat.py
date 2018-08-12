import pandas as pd
import os

files = os.listdir('../data/data/')
# print(len(files))

# for root, dirs, files in os.walk('../data/data'):
#     print(root, dirs, files)

# from os.path import join, getsize
# for root, dirs, files in os.walk('../data/data'):
#     print(sum(getsize(join(root, name)) for name in files))


# data = pd.read_csv(os.path.join('../data/data', files[0]), names = ['userId', 'movieId', 'rating', 'timestamp'])
# print(data.head())

data = pd.DataFrame(columns=['userId', 'movieId', 'rating', 'timestamp'])

for name in files:
     tmp = pd.read_csv(os.path.join('../data/data', name), names = ['userId', 'movieId', 'rating', 'timestamp'])
     data = pd.concat([data,tmp])

print(data.info())
