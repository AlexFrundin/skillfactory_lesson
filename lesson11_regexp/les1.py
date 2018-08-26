from pymystem3 import Mystem

m = Mystem()
i = 0

with open('../data/test_pymy.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split()
        lemmas ="".join(m.lemmatize(word) for word in line)
        print(word,lemmas)
