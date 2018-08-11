def rec(i):
    if i > 1:
        print(i)
        return rec(i-1)
    return 1

data = [
['2018-01-01', 'google', 'cpc', 'ДФО', 'кампания_1', 'Хабаровск', 114],
['2018-01-01', 'google', 'cpc', 'ДФО', 'кампания_2', 'Владивосток', 536],
['2018-01-01', 'google', 'cpc', 'ДФО', 'кампания_1', 'Магадан', 436]
]

data_test = [
    ['2016-10-01', 'google', 'sem', 5],
    ['2016-10-01', 'google', 'seo', 1],
    ['2016-10-01', 'newsletter', 'email', 1]
]

def list_to_dict(data):
    dict2fill = {}

    if len(data)>1:
        dict2fill[data[0]] = list_to_dict(data[1:])
    else:
        return data[0]
    return dict2fill


def checkLevels(line, data_dict={}, level=0):
    if line[level] in data_dict:
        checkLevels(line, data_dict[line[level]], level+1)
        return data_dict
    else:
        data_dict[line[level]] = list_to_dict(line[level+1:])
        return data_dict


def find_line_value(final_dict, line):
    if len(line) > 1:
        if line[0] in final_dict:
            return find_line_value(final_dict[line[0]],line[1:])
        else:
            return 0
    else:
        if line[0] in final_dict:
            return final_dict[line[0]]
        else:
            return 0


data_ = {}
for line in data:
    data_ = checkLevels(line)
print((int(find_line_value(data_, ['2018-01-01', 'google', 'cpc', 'ДФО', 'кампания_2',"Владивосток"]))/26800))
