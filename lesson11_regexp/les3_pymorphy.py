import pymorphy2

morph = pymorphy2.MorphAnalyzer()

# print(morph.parse('стали'))
i=0
with open ("../data/keywords.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split('\t')
        word = line[0]
        word_analyze_morph = morph.parse(word)
        # print(word_analyze_morph)
        print(word_analyze_morph[0].normal_form)
        if i>5:
            break
        i += 1
