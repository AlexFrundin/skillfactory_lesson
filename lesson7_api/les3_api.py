from pprint import pprint
from yaml import load as _
import requests
f = open('../config.yaml', mode = 'r', encoding = 'utf-8')
proxies = {'https':'144.76.62.29:3128',
           'https':'109.197.27.77:3128'}

params = {
  'access_token': _(f)['access_token'],
  'v': 5.73
}

url = 'https://api.vk.com/method/users.get?user_id=1&v=5.52&fields=sex,bdate,country'
r = requests.get(url, proxies=proxies, params=params)

print(r.text)
