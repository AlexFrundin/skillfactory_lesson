def search_for_line(source, orders_dict):
    return orders_dict.get(source,0)

orders_dict = {}
with open('../data/orders_by_source.txt', 'r') as f:
    for line in f:
        line = line.strip().split('\t')
        orders_dict[line[0]]=int(line[1])

with open('../data/visits_by_source.txt', 'r') as f:
    for line in f:
        line = line.strip().split('\t')
        search = line[0]
        orders = search_for_line(search, orders_dict)
        visits = int(line[1])
        print(search, visits, orders, round(orders/visits,3))
