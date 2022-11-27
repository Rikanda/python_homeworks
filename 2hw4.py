n = int(input('Введите значение N: '))
p1 = int(input('Укажите позицию первого числа: '))
p2 = int(input('Укажите позицию второго числа: '))

my_list = []
if n>=0:
    for i in range(-n,n+1):
        my_list.append(i)
    print(my_list)
else:
    n = abs(n)
    for i in range(-n,n+1):
        my_list.append(-i)
    print(my_list)

if(p1>abs(n)*2+1 or p2>abs(n)*2+1):
    print('Нет значений для заданных позиций')
else:
    print(my_list[p1-1]*my_list[p2-1])