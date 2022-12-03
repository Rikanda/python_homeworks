import random
n = int(input('Введите значение N: '))
first_list =[]
second_list =[]

for i in range(0, n):
    first_list.append(i)
print(first_list)

# в первом списке берем элемент со случайным индексом и перекладываем его во второй список, пока первый список не опустеет
while first_list != []:
    random_index = random.randint(0, len(first_list)-1)
    second_list.append(first_list[random_index])
    first_list.pop(random_index)
print(second_list)
