def source_type_classification( line ):
    source = line[5]
    medium = line[4]
    amount_paid = float( line[-1].replace(',', '.') )
    if source == 'google' or source == 'yandex':
        if medium == 'seo' or medium == 'sem':
            sourceType = 'search engines seo'
        elif medium == 'brand':
            sourceType = 'search engines brand'
        else:
            sourceType = 'search engines undefined'
    else:
        sourceType = 'other'
    return sourceType

source_type_stats = {}
with open( 'data/data_no_header.txt', 'r' ) as f:
    for line in f:
        line = line.strip().split('\t')
        sourceType, orderType = source_type_classification( line )
