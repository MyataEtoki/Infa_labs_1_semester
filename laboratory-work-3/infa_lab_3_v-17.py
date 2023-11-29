# доп - Ввести строку и образец,
# вывести на экран только слова
# начинающиеся с заданного образца
string = input('Введите слова через пробел: ')
#sample = input('Введите образец: ')
string = string.split()
alf_consonants_en = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
alf_consonants_ru = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ'
answer = ''
''' Это нафиг тут не надо
for r in range(len(string)): #если мы считаем таб в начале(таб в середине!=пробелы) за 4 пробела, а не за отдельный символ
    if string[r]!= '\t':
        if string[r][0] == '\t':
            string[r] = string[r][1::]
            print(r,string[r][0])
'''
for i in range(len(string)):
    if (string[i][0] in alf_consonants_en) or (string[i][0] in alf_consonants_ru) :
        answer = answer + string[i] + ' '
print('Слова начинающиеся с согласной:',answer)
'''
sample_answer = ''
for k in range(len(string)):
    if string[k] != '' and string[k] != '\t':
        if string[k][0:len(sample)] == sample: #забыл проверку на заканчивание образцом - string[k][-1:len(sample)[0:-1:]] == sample
            sample_answer += string[k] + ' '
print('Слова начинающиеся с образца:', sample_answer)
'''