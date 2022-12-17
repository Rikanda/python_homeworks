from itertools import groupby

name_list =[]
for i in range(6):
    name_list.append(input('Укажите имя: '))
print(name_list)

def first_word(name): 
    return name[0]

sort_list = sorted(name_list, key = first_word)
dict_name = {k: list(vals) for k, vals in groupby(sort_list,first_word)}

print(dict_name)
