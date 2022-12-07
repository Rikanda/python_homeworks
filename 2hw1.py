from decimal import Decimal
# использую Decimal чтобы избежать погрешностей, которые возникают при операциях с float
s = (input('введите любое число '))
f = abs(Decimal(s))

# если ввели 0, то вернется результат 0
result = 0

# увеличиваем разряд числа, чтобы перевести дробную часть в целую: 0.123 => 123.000
while not(f%1)==0:
    f*=10

n = int(f)
# преобразуем число в целое и последовательно суммируем цифры справа налево с помощью модуля от деления на 10: 123 => 3+2+1
while n!=0:
    result +=n%10
    n //=10

print(result)

# второй вариант через строку

result = 0
s1 = s.strip("-")
s2 = s1.replace(".","")
for i in s2:
    result +=int(i)
print(result)

#третий вариант через преобразование в массив
result = 0
s3 = s1.split(".")
for e in range(len(s3)):
    for q in s3[e]:
        result +=int(q)
print(result)





    
 


