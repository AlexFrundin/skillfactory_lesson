from pprint import pprint
from matplotlib import pyplot as plt
import requests
import pandas as pd
from yaml import load as _
f = open('../config.yaml', mode = 'r', encoding = 'utf-8')
token = _(f)['access_token']


def my_request(get, params_, url='https://api.vk.com/method/{}'):
    proxies = {'https':'144.76.62.29:3128',
               'https':'109.197.27.77:3128'}
    params = {
        'access_token': token,
        'v': 5.73,
    }
    params.update(params_)
    r = requests.get(url.format(get), proxies=proxies, params=params)
    return r

get_user = 'users.get'
get_group = 'groups.getMembers'

def params_user(ids: str, fields: str)->dict:
    return  {
            'user_ids': ids,
            'v': 5.73,
            'fields': fields
            }

params_group = {
        'group_id': 'habr',
        'v': 5.73,
        'offset': 1000,
    }

data = my_request(get_group, params_group).json()
users = [str(x) for x in sorted(data['response']['items'])]
users_list = [",".join(users[i:100+i]) for i in range(0,1000,100)]
city_dict ={}

for user in users_list:
    data = my_request(get_user, params_user(user, 'city')).json()['response']
    for info in data:
        try:
            country = info['city']['title']
        except:
            pass
        else:
            try:
                city_dict[country] += 1
            except:
                city_dict[country] = 1

df = pd.DataFrame.from_dict(city_dict, orient = 'index').reset_index()
df.rename(columns = {'index':'city', 0:'users'}, inplace = True)
df = df.sort_values('users', ascending=False)
df['category'] = df.apply(lambda x: x['city'] if x['users'] > 100 else 'other', axis=1)

sf = df.groupby('category').sum()

sf.plot(kind = 'pie', y='users', figsize = (7,7))
plt.show()
