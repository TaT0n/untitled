import math

a = 2
b = 4
c = 2

d = b ** 2 - 4 * a * c
print('дискр = %.2f' % d)
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x1)
    print(x2)
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Корней нет')
