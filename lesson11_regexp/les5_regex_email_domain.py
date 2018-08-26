import re
import pandas as pd

pattern = '([\w\.-]+)@([\w]+(\.ru|\.com)$)'#создание групп для поиска
prog = re.compile(pattern)

# print(re.search(pattern, "username@yandex.ru").groups())

emails = pd.read_csv('../data/email_base.csv', sep='\t', names = ['email'])


emails['domain'] = emails['email'].apply(lambda x: prog.search(x).group(2) if prog.match(x) else 'Wrong')
print(emails[emails['domain']=='Wrong'].count())


#решение преподователей
# def get_email_domain(row):
#     if re.match(pattern, row['email']):
#         return re.search(pattern, row['email']).group(2)
#     else:
#         return 'wrong email'
#
# emails['domain'] = emails.apply(get_email_domain, axis = 1)
#
