from decimal import Decimal

c = (input('введите любое число '))
d = (input('введите точность числа в формате "0.0001" '))
x = len(d)-2
s = float(c)
print(f'{s:.{x}f}')
v = Decimal(c)
v = v.quantize(Decimal(d))
print(v)
