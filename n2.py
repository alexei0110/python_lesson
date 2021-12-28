list_num = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list_num[i] for i in range(1, len(list_num)) if list_num[i] > list_num[i - 1]]

print(new_list)
