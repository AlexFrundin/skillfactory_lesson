import requests
url = 'https://lenta.ru/articles/2018/02/12/olympics2/'
# r = requests.get(url)
# print(r.text)

urls=['https://github.com/error-page.html', 'https://ru.wikipedia.org/error-page.html','https://lenta.ru/error-page.html', 'https://ria.ru/error-page.html']

for url in urls:
    r = requests.get(url)
    print(r.status_code)
