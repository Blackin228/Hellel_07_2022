list_num = [45, 34, 45, 34, 2, 3, 6, 2, 3, 45, 2]
dict_num = {}


def count(list_num):
    for item in list_num:
        if dict_num.get(item, None):
            dict_num[item] +=1
        else:
            dict_num[item] = 1
    return dict_num


count(list_num)
print(list_num)
print(dict_num)
