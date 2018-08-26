import pymorphy2

morph = pymorphy2.MorphAnalyzer()


words = 'Крымский отель Mriya Resort & Spa признали лучшим в мире курортным комплексом для отдыха по версии престижной международной премии World Travel Awards'

for word in words.split():
    analyze = morph.parse(word)
    if 'NOUN' in analyze[0].tag:
        print(analyze[0].normal_form)
