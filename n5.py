proc = input('Введите значение выручки: ')
cost = input('Введите значение издержек: ')

proc = int(proc)
cost = int(cost)

if proc > cost:
    print('Фирма работает с прибылью')
    rent = (proc - cost) / proc * 100
    print(f"Рентабельность фирмы составляет: {rent}")
    cell = input('Введите численность сотрудников: ')
    cell = int(cell)
    pr = rent / cell
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет: {pr}")
elif proc == cost:
    print('Рентабельность фирмы равна 0')
else:
    print('Фирма работает с убытком')