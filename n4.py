number = input('Введите целое положительное число: ')
number = int(number)
count = -1

while number > 10:
    ost = number % 10
    number //= 10
    if ost > count:
        count = ost
print(count)