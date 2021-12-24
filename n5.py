def sum():
    sum_res = 0
    while True:
        number = input('Введите числа или Q для выхода - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(sum_res)


sum()
