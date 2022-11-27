n = int(input('введите целое число больше 0 '))
if n>0:
    res = 1
    for i in range(2, n+2):
        print(res, end = ', ')
        res *=i

    print()
# второй вариант через список, если значения надо сохранить
    my_list =[1]
    for i in range(2,n+1):
        my_list.append(my_list[i-2]*i)
    print(", ".join(map(str,my_list)))

else:
    print('указано некорректное значение')