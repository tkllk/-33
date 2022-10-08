'''
Вводятся три целых числа a, b, c. С помощью условного оператора 
if найти минимальное значение и вывести его на экран.
'''

print('Нахождение минимального значения')

def minNumber(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
    
    
# ТЕСТ
def test():
    print('Тест')
    print(minNumber(1, 2, 3) == 1)
    print(minNumber(2, 1, 3) == 1)
    print(minNumber(3, 1, 2) == 1)
    print(minNumber(3, 2, 1) == 1)
    print(minNumber(1, 1, 3) == 1)
    print(minNumber(3, 3, 1) == 1)
    print(minNumber(3, 1, 3) == 1)
    print(minNumber(2, 3, 1) == 1)

test()

values = input('Введите 3 целых числа: ').split()
a, b, c = [int(x) for x in values]
print('Минимальное значение:', minNumber(a, b, c))
