import requests
url = 'https://lenta.ru/articles/2018/02/12/olympics2/'
# r = requests.get(url)
# print(r.text)

urls=['https://github.com/error-page.html', 'https://ru.wikipedia.org/error-page.html','https://lenta.ru/error-page.html', 'https://ria.ru/error-page.html']
proxies = {'https':'144.76.62.29:3128',
           'https':'109.197.27.77:3128'}
for url in urls:
    r = requests.get(url, proxies=proxies)
    print(r.status_code)
