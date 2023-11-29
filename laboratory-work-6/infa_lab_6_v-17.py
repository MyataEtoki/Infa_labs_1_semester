# 17. Написать программу для сравнения двух текстовых файлов и записи различий в новый текстовый файл.
'''
Считываем 1(old) и 2(new) файлы
Идём по строкам файла -> (по символам строки?) сравниваем строку 1-го файла со строкой 2-го файла
Если символы не равны -> записываем в 3-тий файл (old:что было в 1 файле // new: что в 2)
Иначе: ничего не делаем
Если в 2 файле больше
'''

file1, file2 = open('1.txt', 'r'), open('2.txt', 'r')
file3 = open('3.txt', 'w')
strings1, strings2 = [x.rstrip('\n') for x in file1.readlines()], [x.rstrip('\n') for x in file2.readlines()]
print(strings1, strings2)
min_len = min(len(strings1), len(strings2))
for i in range(min_len):
    if strings1[i] != strings2[i]:
        file3.write(f'string {i} - old: {strings1[i]} // new: {strings2[i]} \n')
dif_len = max(len(strings1), len(strings2)) - min_len
for i in range(min_len, min_len + dif_len):
    file3.write(f'string {min_len + i} - old: None // new: {strings2[i]} \n')

file1.close()
file2.close()
file3.close()
