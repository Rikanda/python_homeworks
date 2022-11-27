my_list = []

n = int(input('введите число '))
sum = 0

for k in range(1, n+1):
    my_list.append(round(((1+1/k)**k), 3))
    sum +=my_list[k-1]

print(my_list)
print(sum)

