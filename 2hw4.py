n = int(input('Введите значение N: '))
p1 = int(input('Укажите позицию первого числа: '))
p2 = int(input('Укажите позицию второго числа: '))

my_list = []
for i in range(-n,n+1):
    my_list.append(i)
print(my_list)

if(p1>n*2+1 or p2>n*2+1):
    print('Нет значений для заданных позиций')
else:
    print(my_list[p1-1]*my_list[p2-1])