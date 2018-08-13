from yaml import load as _
import requests
from pprint import pprint
import json
import pandas as pandas
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

def params_user(ids: str, fields: str)->dict:
    return  {
            'user_ids': ids,
            'v': 5.73,
            'fields': fields
            }

def params_wall(domain):
    return {
        'domain': domain,
        'filter': 'owner',
        'count': 100,
        'offset': 0,
        }

def params_group (domain):
    return {
        'group_id': domain,
        'v': 5.73,
        'offset': 1000,
        }

def save_to_file(get, params_, domain):
    with open(f'{get.split(".")[0] + "_" + domain}.json', 'w') as f:
         json.dump(my_request(get, params_(domain)).json(), f)

def load_to_file(get, domain):
    with open(f'{get.split(".")[0] + "_" + domain}.json', 'r') as f:
        return json.load(f)

get_user = 'users.get'
get_group = 'groups.getMembers'
get_wall = 'wall.get'
domain = ['habr', 'popularmechanics']

def load():
    for d in domain:
        for get in [get_wall,get_group]:
            yield load_to_file(get,d)


def total(wall):
    data = wall['response']['items']
    total = 0
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
        comments = record['comments']['count']
        likes = record['likes']['count']
        reposts = record['reposts']['count']
        total += (comments+likes+reposts)
    return total


if __name__ == '__main__':
    wall_habr, group_habr, wall_pop, group_pop = load()
    total_habr = total(wall_habr)
    total_pop = total(wall_pop)
    count_habr = group_habr['response']['count']
    count_pop = group_pop['response']['count']
    print(count_habr/total_habr, count_pop/total_pop )
