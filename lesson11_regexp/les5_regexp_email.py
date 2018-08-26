import re
import pandas as pd

pattern = '[\w\.-]+@[\w]+(\.ru|\.com)$'
prog = re.compile(pattern)

emails = pd.read_csv('../data/email_base.csv', sep='\t', names = ['email'])
emails['matc'] = emails['email'].apply(lambda e: True if prog.match(e) else False)
print(emails)
