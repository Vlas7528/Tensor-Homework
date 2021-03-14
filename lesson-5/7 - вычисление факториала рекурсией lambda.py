from functools import reduce
while True:
    n=input()
    try:
        n=int(n)
        break
    except:
        print('Неверный формат числа')
print (reduce(lambda x,y:x*y,range(1,n+1)))