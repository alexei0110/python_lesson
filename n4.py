text = input("Введите строку: ")
data = text.split()
num = 1
for el in range(len(data)):
    if len(str(data)) <= 10:
        print(f' {num} {data[el]}')
        num += 1

    else:
        print(f' {num} {data[el] [0:10]}')
        num += 1


