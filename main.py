# Файлы:
# Бинарные (фотки, видео, музыка и т.д.)
# Текстовые

# open("путь до файла", mode="режим_работы", кодировка)
# Путь: абсолютный, локальный
# mode: Чтение(r), Запись(w), Дополнение

file = open("byron.txt", mode="r")
# Методы для чтения файла
# .read() - считывает весь текст из файла
# text = file.read()
# print(text)

# .readlines() - считывает каждую строку создавая список строк
# text_list = file.readlines()
# print(text_list)

# .readline() - считывает одну строку
# text1 = file.readline()
# text2 = file.readline()
# print(text1)
# print(text2)

file.close()

file2 = open("new_file.txt", mode="w", encoding="utf-8")
# Методы для записи в файл
# .write() - записывает указанный текст в одну строку
file2.write("Я первая строка\n")
file2.write("Я вторая строка\n")
file2.write("""Я третья строка
Я четвертая строка\n""")

# .writelines() - записывает список строк в файл
lines_list = [f'{i}-строка\n' for i in range(1, 11)]
file2.writelines(lines_list)

file2.close()


# Режимы бинарныч текстов
# rb - read bytes
# wb - write bytes

# img = open("nature.jpg", mode="rb")
# content = img.read()
# print(content)
#
# img.close()


# with - контекстный менеджер
with open("nature.jpg", mode="rb") as img:
    content = img.read()
    for i in range(10):
        new_img = open(f'img{i}.jpg', mode="wb")
        new_img.write(content)
