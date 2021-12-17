a = input('Введите количество километров в первый день: ')
b = input('Введите количество километров: ')
count = 1

a = int(a)
b = int(b)

while a <= b:
    a = a * 1.1
    count +=1

print(count)