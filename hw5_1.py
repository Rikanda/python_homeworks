import random

def create_list(k:int):
    words = []
    s = list('абв')
    if k>0:
        for i in range(k):
            random.shuffle(s)
            word = "".join(s)
            words.append(word)    
    return words

full_list = create_list(int(input('укажите количество слов ')))

new_list = [v for v in full_list if v!='абв']

if full_list:
    print(" ".join(full_list))
    print(" ".join(new_list))
else:
    print('некорректные данные')