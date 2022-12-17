from random import choices

def create_list(num: int):
    list = choices(range(num*2), k = num)
    print(list)
    return list

list1 = create_list(int(input('введите число')))

finish_list = [j for i, j in zip(list1, list1[1::]) if j>i]
print(finish_list)