with open('text.txt', 'w', encoding='utf-8') as f_obj:
    while True:
        line = input('Введите новую строку - ')
        if not line:
            break
        f_obj.write(f'{line}\n')