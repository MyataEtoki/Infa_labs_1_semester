# 17. Написать программу для сравнения двух текстовых файлов и записи различий в новый текстовый файл. (сходства не смотрит)
'''
Считываем 1(типа old) и 2(типа new) файлы
Идём по строкам файла -> (по символам строки?) сравниваем строку 1-го файла со строкой 2-го файла
Если символы не равны -> записываем в 3-тий файл (old:что было в 1 файле // new: что в 2)
Иначе: ничего не делаем
Если в 2 файле больше строк, чем в 1, то дописываем это в конец 3 файла.
'''

file1, file2 = open('1.txt', 'r'), open('2.txt', 'r')
file3 = open('3.txt', 'w')
strings1, strings2 = [x.rstrip('\n') for x in file1.readlines()], [x.rstrip('\n') for x in file2.readlines()]
# rstrip() - удаляет заданные символы в конце строки (по-умолч. пробелы)
min_len = min(len(strings1), len(strings2))
max_len = max(len(strings1), len(strings2))
for i in range(min_len):
    if strings1[i] != strings2[i]:
        file3.write(f'string {i+1} - 1 file: {strings1[i]} // 2 file: {strings2[i]} \n')
        # i+1 ради смотрибельности, т.к текст.ред. считает с 1, а не с 0
if len(strings2) > len(strings1):
    for i in range(min_len, max_len):
        file3.write(f'string {i+1} - 1 file: None // 2 file: {strings2[i]} \n')
else:
    for i in range(min_len, max_len):
        file3.write(f'string {i+1} - 1 file: {strings1[i]} // 2 file: None \n')

file1.close()
file2.close()
file3.close()
