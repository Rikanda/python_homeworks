n = int(input('введите число больше чем 20: '))
my_list = [i for i in range(20,n+1) if i%20==0 or i%21 == 0]
print(my_list)