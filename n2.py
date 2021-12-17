num_1 = input('Введите время в секундах: ')
num_1 = int(num_1)

h = num_1 // 3600
ost_1 = num_1 - h * 3600
m = ost_1 // 60
s = ost_1 - m * 60

print(f"{h}:{m}:{s}")