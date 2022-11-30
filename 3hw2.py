import random
n=abs(int(input('укажите количество чисел ')))

my_list = []
pairs_list = []
while(len(my_list)<n):
    my_list.append(random.randint(1,10))
print(my_list)

i=0
while len(pairs_list)<(n/2)-1:  
    pairs_list.append(my_list[i]*my_list[len(my_list)-1-i])
    i +=1

if n/2>0:
    pairs_list.append(my_list[n//2])

print(pairs_list)
