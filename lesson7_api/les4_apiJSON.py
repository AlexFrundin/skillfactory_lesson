from pprint import pprint
import requests
import requests
from yaml import load as _
f = open('../config.yaml', mode = 'r', encoding = 'utf-8')
proxies = {'https':'144.76.62.29:3128',
           'https':'109.197.27.77:3128'}

users = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user = 1
token = _(f)['access_token']
def get_params(user):
    return {
            'access_token': token,
            'v': 5.73,
            'user_id':user,
            'fields':'sex,bdate,country',
            }

url = 'https://api.vk.com/method/users.get'
male = 0
female = 0

for user in users:
    r = requests.get(url, proxies=proxies, params=get_params(user))
    data = r.json()
    print(data)
    data = data['response'][0]['sex']
    if data == 2:
        male += 1
    elif data == 1:
        female += 1
print(male, female, female/(male+female))
