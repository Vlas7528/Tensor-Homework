from decimal import Decimal
def bank(sum, percent, months):
    for i in range(months):
        print (f'Сумма вклада за месяц {i+1} выросла на {round(((sum*percent)/100), 3)}')
        sum = sum + ((sum * percent) / 100)
        print (f'и составила {round(sum, 3)} рублей\n')
    return sum

while True:
    sum = input ('Введите сумму вклада в рублях -> ')
    percent = input ('Введите значение начисляющихся процентов каждый месяц -> ')
    months = input ('Введите количество месяцев (цело число) -> ')
    print('*** Проверка введенных чисел... ***')
    try: 
        sum = Decimal(sum)
        percent = Decimal(percent)
        months = int(months)
        break
    except Exception as e:
        print('Неверный формат введенных чисел. Повторите ввод.')
        
print(f'Рассчитанная сумма вклада: {round(bank(sum, percent, months), 3)} рублей')
