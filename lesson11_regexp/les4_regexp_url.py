import re

pattern = '.*/[0-9]{8}-.*'

prog = re.compile(pattern)

with open('../data/urls.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if prog.match(line):
            print(line)
