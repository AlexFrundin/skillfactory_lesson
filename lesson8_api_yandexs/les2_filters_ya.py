from yaml import load as _
import requests
from pprint import pprint
import json
import pandas as pandas


with open('../config.yaml', 'r') as f:
    token = _(f)['token_yandex']
counter = '21075004'

startDate = '2018-02-12'
endDate = '2018-02-18'
dimensions = ['ym:s:date']
metrics = ['ym:s:visits', 'ym:s:users', 'ym:s:pageviews', 'ym:s:percentNewVisitors']
metrics_string = ','.join(metrics)
dimensions_string = ','.join(dimensions)
preset = 'traffic'
filters = "ym:s:regionCountryName=='Россия'"

def my_request(params_={}, get='', url='https://api-metrika.yandex.ru/stat/v1/data'):
    proxies = {'https':'185.85.162.32:81',
                'https':'5.128.60.74:3128'}
    params = {
            'date1': startDate,
            'date2': endDate,
            'metrics':metrics[0],
            'id': counter,
            'preset': preset,
            'oauth_token': token,
                }
    params.update(params_)
    r = requests.get(url.format(get), proxies=proxies, params=params)
    return r

data = my_request(params_={'filters':filters}).json()
ru = data['data'][0]['metrics'][0]
data = my_request().json()
all = data['data'][0]['metrics'][0]
print(ru/all)
