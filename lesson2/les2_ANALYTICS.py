cpa_commission = {'burgerclub': 0.3,'food-delivery': 0.25}
cpc_commission = {'city-magazine': 7,'foody': 9}
fixed_commission = 4
def costs_classification( amount_paid, source ):
    if source in cpa_commission:
        return amount_paid * cpa_commission[ source ]
    if source in cpc_commission:
        return cpc_commission[ source ]
    return fixed_commission
def expense_and_income( line ):
    source = line[5]
    amount_paid = float( line[-1].replace( ',', '.' ) )
    cost = float( line[6].replace( ',', '.' ) )
    partner_comission = costs_classification(amount_paid,source )
    return source, cost + partner_comission, amount_paid
roi_stats = {}
with open( 'data/data_no_header.txt', 'r' ) as f:
    for line in f:
        line = line.strip().split('\t')
        source, cost, income = expense_and_income( line )
        if source in roi_stats:
            roi_stats[ source ][ 'cost' ] += cost
            roi_stats[ source ][ 'income' ] += income
        else:
            roi_stats[ source ] = {}
            roi_stats[ source ][ 'cost' ] = cost
            roi_stats[ source ][ 'income' ] = income

for source, data in roi_stats.items():
    data['roi'] = ( data['income'] - data['cost'] ) / data['cost']
for source, data in roi_stats.items():
    print( '{}\t{:.2f}'.format( source, data['roi'] ) )
