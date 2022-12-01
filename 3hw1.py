import random
n=abs(int(input('укажите количество чисел ')))

my_list = []
sum = 0
while(len(my_list)<n):
    my_list.append(random.randint(1,10))
    if len(my_list)%2 != 0:
        sum +=my_list[(len(my_list)-1)]

print(my_list)
print(sum)