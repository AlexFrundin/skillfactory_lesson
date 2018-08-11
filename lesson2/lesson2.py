with open('data/user_ids.txt', "r") as f:
    user_ids=[line.strip() for line in f]
with open("data/user_ids_headers.txt","r") as f:
    pass
total_amount = 0
with open("data/data_3_columns.txt","r") as f:
    for line in f:
        line = line.strip().split()
        medium = line[0]
        source = line[1]
        if source == 'yandex' and medium == 'seo':
            amount_paid = float(line[2].replace(',', '.'))
            total_amount+=amount_paid
print(total_amount)
