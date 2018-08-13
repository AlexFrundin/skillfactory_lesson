from yaml import load as _
import requests
from pprint import pprint
import json


def first():
    with open('../config.yaml', 'r') as f:
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
    get_wall = 'wall.get'

    params_group = {
        'domain': 'habr',
        'filter': 'owner',
        'count': 100,
        'offset': 0,
    }


    return my_request(get_wall, params_group)
    # with open('data.json', 'w') as f:
    #     json.dump(my_request(get_wall, params_group).json(), f)

# data  = first().json()

with open('data.json', 'r') as f:
    data = json.load(f)


data = data['response']['items']
stats ={}
for record in data:
    if 'attachments' in record:
        if 'link' in record['attachments'][0]:
            title = record['attachments'][0]['link']['title']
        elif 'photo' in record['attachments'][0]:
            title = record['attachments'][0]['photo']['text']
    elif 'copy_history' in record:
        if 'link' in record['copy_history'][0]['attachments'][0]:
            title = record['copy_history'][0]['attachments'][0]['link']['title']
        elif 'poll' in record['copy_history'][0]['attachments'][0]:
            title = record['copy_history'][0]['attachments'][0]['poll']['question']
    stats[title] = [
        record['comments']['count'],
        record['likes']['count'],
        record['reposts']['count'],
        (record['date']),
                    ]
# stats = sorted(stats.items(), key=lambda x: -(x[1][0]+x[1][1]+x[1][2]))
stats = {key[:35]:value for key, value in stats.items()}
from datetime import datetime, timedelta

for title, line in stats.items():
    line.append(datetime.fromtimestamp(line[3]).strftime('%Y-%m-%d'))

yesterday = (datetime.now() - timedelta(days = 1)).strftime('%Y-%m-%d')

for key, value in sorted(stats.items(), key=lambda s: -(s[1][0]+s[1][1]+s[1][2])):
    if value[4] == yesterday:
        print(key, value)
