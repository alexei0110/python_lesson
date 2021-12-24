def int_func (*args):
	word = input("Введите слово: ")
	print(word.title())
	return


int_func()


def capitalize(word):
	first_letter_small = word[0]
	first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
	return first_letter_big + word[1:]


source = input("Введите несколько слов: ").split()
res = []
for word in source:
	res.append(capitalize(word))
print(' '.join(res))
