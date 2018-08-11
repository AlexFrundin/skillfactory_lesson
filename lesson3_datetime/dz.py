from datetime import datetime
users_info = {}
with open( '../data/data_no_header.txt', 'r' ) as f:
    for line in f:
        line = line.strip().split('\t')
        # дата транзакции, по максимальному и минимальному значению которой будем считать LT
        dateTime = datetime.strptime( line[1], '%d.%m.%Y %H:%M' )
        user_id = line[2]
        # сумма покупки
        amount_paid = float( line[8].replace(',', '.') )
        try:
            users_info[user_id] += amount_paid
        except:
            users_info[user_id] = amount_paid
total = sum(users_info.values())
count = len(users_info)

print(round(total/count))
