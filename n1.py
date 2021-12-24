a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

def func (a, b):
    if b == 0:
        return "Делитель не может быть равен нулю"
    else:
        res = a / b
        return res


print(func(a, b))
