from itertools import groupby

# компрессия строки
def compress(string):
    for char, same in groupby(string):
        count = sum(1 for _ in same)
        yield str(count) + char

# декомпрессия строки
def decompress(string):
    decode = ''
    count = ''
    for char in string:
        if char.isdigit():
            count +=char
        else:
            decode +=char*int(count)
            count = ''
    return decode

# чтение любого файла в виде массива записей строк
def read_file(name:str):
    lines =[]
    rf = open(name,'r')
    for L in rf.readlines():
        lines.append(L)
    return lines

# запись сжатых строк в файл
def write_file(name1:str, name2:str):
    lines = read_file(name1)
    with open (name2,'a',encoding='utf-8') as F:
        for i in range(len(lines)):
            string = str(lines[i]).strip("\n")
            res = ''.join(compress(string))
            F.writelines(f'{res}\n')

# декодирование и вывод в консоль строк из сжатого файла
def print_file(name:str):
    lines = read_file(name)
    for i in range(len(lines)):
        string = str(lines[i]).strip("\n")
        res = decompress(string)
        print(res)


file1_name = input('введите имя файла с текстом: ')

file2_name = input('введите имя файла с сжатым текстом: ')

write_file(file1_name, file2_name)

print_file(file2_name)