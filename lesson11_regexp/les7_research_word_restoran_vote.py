from nltk.stem import SnowballStemmer

snow = SnowballStemmer("russian")


from yaml import load

params = load(open('../data/params.yaml', mode='r', encoding='utf-8'))#берем список слов оценок



def clear_punctuation(text):
    symbols = '.,!()"<>'
    spaces = ' '*len(symbols)
    return text.translate(text.maketrans(symbols, spaces))


# text_from = clear_punctuation('Просто шикарный клуб! Ходили с другом на "Animal Джаz"! Остались очень довольны, атмосфера очень уютная, дружелюбная, есть второй этаж, бар')

def classifier(text):
    text_from = clear_punctuation(text)

    positive_worlds_list = [
        x for x in text_from.split()
        if snow.stem(x) in params['positive']
        ]

    negative_worlds_list = [
        x for x in text_from.split()
        if snow.stem(x) in params['negative']
    ]

    positive_count = len(positive_worlds_list)
    negative_count = len(negative_worlds_list)

    if negative_count<positive_count:
        return 'positive'
    elif negative_count>positive_count:
        return 'negative'
    else:
        return 'undef'



with open('../data/texts_opinions.txt', 'r', encoding='utf-8') as f_in:
    with open('../data/text_classified.txt', 'w') as f_out:
        for line in f_in:
            line = line.strip()
            f_out.write(f'{classifier(line)}\n')
