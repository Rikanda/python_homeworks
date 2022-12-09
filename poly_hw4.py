from random import choices

# собираю массив коэффициентов
def create_list(num: int):
    list = choices(range(0,11), k = num)
    return list

# определяю знак аргумента случайным образом
def sign():
    ask = choices(range(0,2),k=1)
    if ask[0]==0:
        return " + "
    else:
        return " - "

# записываю строку в файл
def poly(k: int, fn: str):
    list1=create_list(k+1)
    with open (fn,'a',encoding='utf-8') as F:
        if k>1 or (k ==1 and list1[1]!=0):
            line = str(list1[0])+" = 0"
            for i in range(1,len(list1)):
                if list1[i]!=0:
                    l = str(list1[i]) + "*x^" + str(i) + sign()
                    line = l+ line 
            F.writelines([f'{line}\n'])