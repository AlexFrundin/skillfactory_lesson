def source_type_classification( source, medium ):
    """
    Функция классифицирует источник трафика в зависимости от значения source и medium.
    Возвращает название типа источника по правилам:
        - если source равен 'google' или 'yandex', то проверяем medium:
            - для medium 'seo' или 'sem' возвращаем 'search engines seo'
            - для medium 'brand' - возвращаем 'search engines brand'
            - для остальных случаев возвращаем 'search engines undefined'
        - если условие не выполнено, то возвращаем 'other'
    """
    if source == 'google' or source == 'yandex':
        if medium == 'seo' or medium == 'sem':
            return 'search engines seo'
        elif medium == 'brand':
            return 'search engines brand'
        else:
            # если вдруг встретится другой вариант, то ставим "undefined"
            return 'search engines undefined'
    else:
        return 'other'

source_type_stats = {}

with open( 'data/data_no_header.txt', 'r' ) as f:
    for line in f:
        line = line.strip().split('\t')
        source = line[5]
        medium = line[4]
        sourceType = source_type_classification( source, medium )
        if sourceType in source_type_stats:
            source_type_stats[ sourceType ] += 1
        else:
            source_type_stats[ sourceType ] = 1
print(source_type_stats)
