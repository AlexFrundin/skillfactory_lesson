from pprint import pprint

def search_for_line(source, medium, orders_dict):
    print(source, medium)
    return  0 if not orders_dict.get(source,0) else orders_dict.get(source,0).get(medium, 0)


orders_dict = {}
with open('../data/orders_by_source_and_medium.txt', 'r') as f:
    for line in f:
        line = line.strip().split('\t')
        source = line[0]
        medium = line[1]
        count = int(line[2] )

        orders_dict.setdefault(source, {})

        orders_dict[source].setdefault(medium, 0)

        orders_dict[source][medium] = count


pprint(orders_dict)

print(search_for_line('google', 'seo', orders_dict))
print(search_for_line('google_123', 'seo', orders_dict))
print(search_for_line('google', 'seo_123', orders_dict))
print(search_for_line('google', 'sem', orders_dict))
