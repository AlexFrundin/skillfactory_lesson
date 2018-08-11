from datetime import datetime, timedelta
def LT_calculation(uid_transactions):
    if uid_transactions[0][1]>100:
        first_order = uid_transactions[1]
    else:
        first_order = uid_transactions[0]
    last_order = uid_transactions[-1]
    first_order_date = first_order[0]
    last_order_date = last_order[0]
    return (last_order_date-first_order_date).days


Started = True
user_info = {}
user_id_transactions = []
LT_days = 0
LT_users = 0
with open( '../data/data_no_header.txt', 'r' ) as f:
    for line in f:
        line = line.strip().split('\t')
        # дата транзакции, по максимальному и минимальному значению которой будем считать LT
        dateTime = datetime.strptime( line[1], '%d.%m.%Y %H:%M' )
        user_id = line[2]
        # сумма покупки
        amount_paid = float( line[8].replace(',', '.') )

        if Started:
            previous_user_id = user_id
            user_id_transactions = [[dateTime, amount_paid]]
            Started = False
        else:
            if user_id == previous_user_id:
                user_id_transactions.append([dateTime,amount_paid])
            else:
                LT_days_for_current_user = LT_calculation( user_id_transactions )
                if (LT_days_for_current_user+1)>0:
                    LT_days += LT_days_for_current_user
                    LT_users += 1
                previous_user_id = user_id
                user_id_transactions = [[dateTime, amount_paid]]
    LT_days_for_current_user = LT_calculation( user_id_transactions )
    if (LT_days_for_current_user+1a) > 0:
        LT_days += LT_days_for_current_user
        LT_users += 1
print('Lifetime = {:.1f} days'.format( LT_days / LT_users ))
