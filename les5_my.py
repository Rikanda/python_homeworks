from random import choices

def create_list(num: int):
    list = choices(range(num*2), k = num)
    print(list)
    return list

list1 = create_list(int(input()))

# мой вариант

# функция реализует логику формирования элемента для нового массива
def f(x,L):    
    val = L[x]
    sub_list =[]
    list2 = L[x::]
    for j in range(len(list2)):
        if list2[j]>val:
            val = list2[j]
            sub_list.append(val)
    if sub_list:
        sub_list.insert(0,L[x])
    return sub_list


# формирование нового массива на основе заданного массива
new_list = [f(i, list1) for i in range(0, len(list1)) if f(i,list1)]
print(new_list)


# ваниант с семинара
# from random import choices
# def create_list(number_1):
#     list = choices(range(number_1*2), k = number_1)
#     return list
# second_list = create_list(int(input()))
# print(second_list)

# def collector (second_list):
#     therd_list = []
#     for i in range(len(second_list)):
#         value = second_list[i]
#         sublist_list = [value]
#         for k in range(i + 1, len(second_list)):
#             if second_list [k] > value:
#                 value = second_list [k]
#                 sublist_list.append (value)
#         if len (sublist_list) > 1:
#             therd_list.append (sublist_list)
#     return therd_list 
# print(collector(second_list))