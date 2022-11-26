x = int(input('Укажите значение х: '))
y = int(input('Укажите значение y: '))
if x == 0 or y == 0:
    print(' Вы ввели 0, это недопустимое значение') 
elif x>0 and y>0:
    print (1)
elif x<0 and y>0:
    print (2)
elif x<0 and y<0:
    print (3)
else: 
    print (4)