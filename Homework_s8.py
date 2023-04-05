file_path = r'new_text.txt'

# Чтение всего файла
def reading_al_file(file_path):
    with open(file_path,'r') as f:
        for line in f:
            print(line)

# Добавление информациии
def append_in_file(file_path):
    with open(file_path, 'a') as f:
        message_1 = input("Введите ФИО и телефон: ")
        f.write("\n" + message_1)

# Поиск данных в файле
def find_in_file(file_path):
    some_to_find = input("Что мы ищем: ")
    with open(file_path, 'r') as f:
        for line in f:
            if some_to_find.casefold() in line.casefold():
                print(line)

# Изменение уже существующих записей
def change_info(file_path):
    some_to_change = input("Что нужно заменить? ")
    new_info = input("На что меняем? ")
    with open(file_path,'r') as f:
        table_t = f.read()
        if some_to_change in table_t:
            table_t = table_t.replace(some_to_change, new_info)
    with open(file_path, 'w+') as f:
        f.write(table_t)


# Вызов функции
change = input("Выберите действие с файлом. 1 - чтение, 2 - добавление, 3 - поиск, 4 - изменение существующей записи.   ")

if change == "1":
    reading_al_file(file_path)
if change == '2':
    append_in_file(file_path)
if change == '3':
    find_in_file(file_path)
if change == '4':
    change_info(file_path)