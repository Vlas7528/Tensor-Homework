from math import sqrt
from decimal import Decimal
import decimal


def quadratic_equation(fa, sa, ta):
    D = Decimal(sa ** 2 - 4 * (fa * ta))
    print ('D =', D)
    if D == 0:
        print('Дискриминант равен нулю, есть только один корень')
        x = Decimal(-sa / (2 * fa))
        print ('Корень найден: ', x, ' \nРешение завершено.')
    elif D > 0:
        print('Дискриминант больше нуля, есть два корня')
        x1 = (-sa + Decimal(sqrt(D))) / (2 * fa)
        x2 = (-sa - Decimal(sqrt(D))) / (2 * fa)
        print ('Корни найдены: x1 =', x1, ' x2 =', x2, '\nРешение завершено')
    else:
        print('Дискриминант меньше нуля, корней нет. Решение завершено.')
    
