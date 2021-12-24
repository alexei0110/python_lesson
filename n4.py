def my_func(x,y):
    res1 = x ** y
    res2 = 1
    i = 1
    while i <= abs(y):
        res2 *= x
        i += 1
    return res1, 1 / res2


print(my_func(float(input('Введите основание: ')), int(input('Введите степень: '))))
