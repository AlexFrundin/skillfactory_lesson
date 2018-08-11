def search_for_line(source, orders_dict):
    return orders_dict.get(source,0)

orders_dict = {}
with open('../data/orders_by_source.txt', 'r') as f:
    for line in f:
        line = line.strip().split('\t')
        orders_dict[line[0]]=int(line[1])

summa = 0
count = 0
with open('../data/joined_by_source.txt', 'w') as f_in:
    with open('../data/visits_by_source.txt', 'r') as f:
        for line in f:
            line = line.strip().split('\t')
            source = line[0]
            orders = search_for_line(source, orders_dict)
            visits = int(line[1])
            avg = round(orders/visits, 3)
            summa += avg
            count += 1
            f_in.write(f'{source}\t{visits}\t{orders}\t{avg}\n')
print(summa/count)
