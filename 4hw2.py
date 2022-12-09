from math import sqrt
import math

n = abs(int(input('введите любое натуральное число ')))
l=[]
if n ==1:
    l.append(1)

elif n >1 :
    a = math.ceil(sqrt(n))
    for i in range(2,a):
        while n%i == 0:
            l.append(i)
            n /=i

print(l)


    

