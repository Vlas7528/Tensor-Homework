print('Для решения квадратного уравнения вида ax^2 + bx + c = 0 введите коэффициенты')
from Les2_Module import quadratic_equation
#Используем тип данных decimal
from decimal import Decimal
#Для расчёта квадратных корней вызываем sqrt
from math import sqrt
import decimal

a=Decimal(input('Введите коэффициент a -> '))
b=Decimal(input('Введите коэффициент b -> '))
c=Decimal(input('Введите коэффициент c -> '))

print ('a: ', a, 'b: ', b, 'c: ', c)

# Для начала нам нужно определить дискриминант
quadratic_equation(fa = a, sa = b, ta = c)

# После определения дискриминанта, сравниваем его с нулём, чтобы понять сколько корней имеет данное квадратное уравнение
