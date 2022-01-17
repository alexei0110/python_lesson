lines_n = 0
words_n = 0
with open("test_2.txt", 'r', encoding='utf-8') as file_obj:
    for line in file_obj:
        lines_n += 1
        words = line.split()
        words_n += len(words)

print(lines_n)
print(words_n)