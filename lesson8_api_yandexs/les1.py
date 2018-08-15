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

def my_request(get='', params_={}, url='https://api-metrika.yandex.ru/stat/v1/data'):
    proxies = {'https':'185.85.162.32:81',
                'https':'5.128.60.74:3128'}
    params = {
            'date1': startDate,
            'date2': endDate,
            'id': counter,
            'preset': preset,
            'oauth_token': token
                }
    params.update(params_)
    r = requests.get(url.format(get), proxies=proxies, params=params)
    return r

data = my_request().json()
pprint(data)
# for line in data['data']:
#     visit_date = line['dimensions'][0]['name']
#     visits = line['metrics'][0]
#     users = line['metrics'][1]
#     pageviews = line['metrics'][2]
#     percent_new_visitors = line['metrics'][3]
#     print(visit_date, visits, users, pageviews, percent_new_visitors)
