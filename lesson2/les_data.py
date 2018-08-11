Started = True
total_amount = 0
allowedMedium = [ 'brand', 'seo' ]
allowedSource = 'yandex'
with open( 'data/data.txt', 'r' ) as f:
    for line in f:
        if Started:
            Started = False
        else:
            line = line.strip().split('\t')
            medium = line[4]
            source = line[5]
            if source == allowedSource and medium in allowedMedium:
                amount = float( line[-1].replace(',', '.') )
                total_amount+=amount
print(total_amount)
