# campaign_stats = {
# 'google': { 'cost': 1000, 'clicks': 500 },
# 'yandex': { 'cost': 1500, 'clicks': 900 }
# }
#
# for campaign, stats in campaign_stats.items():
#     print( 'Кампания {}, цена клика {:.2f} USD'.format( campaign, stats['cost'] / stats['clicks'] ) )

Started = True
unique_user_ids = 0
users_stats_dict = {}
with open( 'data/data_no_header.txt', 'r' ) as f:
    for line in f:
        line = line.strip().split('\t')
        source = line[5]
        medium = line[4]
        if source == 'google' or source == 'yandex':
            if medium == 'seo' or medium == 'sem':
                sourceType = 'search engines seo'
            elif medium == 'brand':
                sourceType = 'search engines brand'
            else:
                # если вдруг встретится другой вариант, то ставим "undefined"
                sourceType = 'search engines undefined'
        else:
            sourceType = 'other'
print(sourceType)
