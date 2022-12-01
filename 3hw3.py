n=abs(int(input('введите целое десятичное число ')))

res=0
i=0
while n!=0:
    res += (n%2)*(10**i)    
    n = n//2
    i +=1

print(res)

