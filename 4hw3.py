from random import choices

def create_list(num: int):
    list = choices(range(0,num), k = num)
    return list


n = int(input('введите количество элементов '))
if n<=0:
    print('введено некорректное значение')
else:
    list1 = create_list(n)
    print(list1)

    new_list = [x for x in list1 if list1.count(x)==1]
    print(new_list)