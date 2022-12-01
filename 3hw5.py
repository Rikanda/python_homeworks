def GetFibonacci (n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        res = 1
        f1 = 1
        f2 = 1
        for i in range(2,n):
            res = f1+f2
            f1 = f2
            f2 = res
            i +=1
        return res
    
def GetFibonacciArray (n):
    fArray = [0]
    i = 1
    while i<n+1:
        fArray.append(GetFibonacci(i))
        fArray.insert(0, GetFibonacci(i)*((-1)**(i+1)))
        i +=1
    return fArray

n = abs(int(input('введите число: ')))
print(GetFibonacciArray(n))

# второй вариант вычисления числа Фибоначчи через рекурсию
def GetFibonacciR(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return GetFibonacciR(n-1)+GetFibonacciR(n-2)

print(GetFibonacciR(n))

