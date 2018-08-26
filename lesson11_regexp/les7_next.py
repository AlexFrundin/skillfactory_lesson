f_classified = open('../data/text_classified.txt', mode = 'r', encoding = 'utf-8')

f_ratings = open('../data/texts_ratings.txt', mode = 'r', encoding = 'utf-8')

classified_list = [line.strip() for line in f_classified]

ratings_list = [line.strip() for line in f_ratings]

right_classifications = 0

total_defined_ratings = 0

for i in range(len(classified_list)):
    if classified_list[i] != 'undef':
        total_defined_ratings += 1
        if classified_list[i] == ratings_list[i]:
            right_classifications += 1

print('Доля верно классифицированных отзывов: {:.0%}'.format(right_classifications / total_defined_ratings))

f_classified.close()
f_ratings.close()
