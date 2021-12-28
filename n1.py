from sys import argv

script_name, worked_hour, rate, benefit = argv

calc = (int(worked_hour) * int(rate)) + int(benefit)

print(f'Заработная плата сотрудника составляет: {calc}')
