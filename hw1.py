

def workday():
    print('Рабочий день')
def weekend():
    print('Выходной')
def default():
    print('Это не день недели!')

day = int(input('Укажите номер дня недели, где 1 это понедельник: '))

# первый вариант решения
match day:
    case 1 | 2 | 3 | 4 | 5:
        workday()
    case 6 | 7:
        weekend()
    case _:
        default()

# второй вариант решения
if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
    workday()
elif day == 6 or day == 7:
    weekend()
else:
    default()
    











        