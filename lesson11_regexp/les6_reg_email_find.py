import re

pattern = '([\w\.-]+)@([\w]+(\.ru|\.com))'#создание групп для поиска
prog = re.compile(pattern)

text = 'Андрей Марков страхование markov_chains@yandex.ru. Мария Кюри технологии mary_decay@gmail.com Петр Капица онлайн-образование study-hard@rambler.ru'

print(re.findall(pattern, text))
print(prog.findall(text))


pattern = '([\w\.-]+@([\w]+)[\.ru|\.com]+)'#создание групп для поиска
prog = re.compile(pattern)

print(prog.findall(text))
