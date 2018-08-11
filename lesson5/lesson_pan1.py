import pandas as pd
import matplotlib.pyplot as plt

# data = pd.read_csv('../data/ratings.csv', dtype={'userId':str, 'movieId':str})
# print(data.head(20))

# data = pd.read_csv('../data/movies.csv')
#
# print(data.info())
# print(data.describe())

# data = pd.read_csv('../data/movies.csv')

# print(data['rating'].mean())


data = pd.read_csv('../data/ratings.csv')

def histogram(data, n_bins=20, cumulative=False, x_label = "", y_label = "", title = ""):
    _, ax = plt.subplots()
    ax.hist(data, bins = n_bins, cumulative = cumulative, color = '#539caf')
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    plt.show()


histogram(data['rating'])
