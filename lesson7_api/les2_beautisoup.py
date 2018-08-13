from bs4 import BeautifulSoup
from pprint import pprint
import requests
proxies = {'https':'144.76.62.29:3128',
           'https':'109.197.27.77:3128'}
r = requests.get(url, proxies=proxies)

url = 'https://lenta.ru/articles/2018/02/12/olympics2/'
soup = BeautifulSoup(r.text, 'html.parser')
topic_title = soup.find(class_='b-topic__title').text
topic_info = soup.find('div', class_='b-topic__info')
topic_date = topic_info.find(class_ = 'g-date').text
article_content = soup.find( itemprop = 'articleBody' ).text
# print(soup.find(class_ = 'b-topic__content').text)
print(soup.find(class_ = 'name').text)
print(soup.find(class_ = 'b-topic__content__author').text)

for link in soup.find( itemprop = 'articleBody' ).find_all( 'a' ):
    print( link.get('href'))

# print(soup)
# print(soup.title)
# print(soup.title.text)

# url2 = 'https://habrahabr.ru/post/348890/'
#
# r = requests.get(url2)
# soup = BeautifulSoup(r.text, 'html.parser')
# pprint(soup.title.string)
