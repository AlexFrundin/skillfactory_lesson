from pprint import pprint
import requests

from yaml import load as _
f = open('../config.yaml', mode = 'r', encoding = 'utf-8')

proxies = {'https':'144.76.62.29:3128',
           'https':'109.197.27.77:3128'}
count = 5
offset = 0
params = {
    'access_token': _(f)['access_token'],
    'group_id': 'habr',
    'v': 5.73,
    'count': count,
    'offset': 1000000,
}
url = 'https://api.vk.com/method/groups.getMembers'
r = requests.get(url, proxies=proxies, params=params)

data = r.json()
print(data)
