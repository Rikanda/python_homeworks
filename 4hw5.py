import poly_hw4
from random import choice
import linecache

# выбор случайного значения
def randomise(x):
    res = choice(range(1,x+1))
    return res

# расчет количество строк в файле
def count_lines(name:str):
    fr = open (name,'r')
    L = fr.readlines()
    return len(L) 

# формировать итоговый файл как сумму многочленов в строках    
def sum_files(flist:list):  
    if count_lines(flist[0])!=count_lines(flist[1]):
        print('данные не матчатся, количество строк в файлах не равно')
    else:
        file_name_sum = input('укажите название итогового файла ')+'.txt'
        with open (file_name_sum,'a',encoding='utf-8') as F:
            for i in range(1,count_lines(flist[0])+1):
                L1 = linecache.getline(flist[0],i).rstrip("= 0\n") + " + " + linecache.getline(flist[1],i).rstrip("\n")
                F.writelines([f'{L1}\n'])
        F.close()
        return

files_list =[] # список сравниваемых файлов

for j in range(2):
    file_name = input('укажите название файла ')+'.txt'
    files_list.append(file_name)
    st = randomise(3)# определяем максимум количество строк
    for i in range(st):  
        k = randomise(10)  # определяем максимум степень
        poly_hw4.poly(k, file_name)

sum_files(files_list)
