from nltk.stem import SnowballStemmer

snowball = SnowballStemmer("russian")

i=0
with open ("../data/keywords.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split('\t')
        word = line[0]
        stem = snowball.stem(word)
        print(word,"->", "".join(stem))
        if i>10:
            break
        i += 1
