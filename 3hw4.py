import random
from math import floor

n=abs(int(input('укажите количество чисел ')))
if n == 0:
    print('вы ввели недопустимое значение')
else:
    my_list = []
    while(len(my_list)<n):
        my_list.append(round((random.randint(1,1000)/100),2))
        k = round((my_list[len(my_list)-1] - floor(my_list[len(my_list)-1])),2)

        if len(my_list)-1 == 0:
            min = k
            max = k    
        elif k<min:
            min=k
        elif k>max:
            max=k
    print(my_list)
    print('Min: {}, Max: {}. Difference: {}'.format(min, max,round(max-min,2)))