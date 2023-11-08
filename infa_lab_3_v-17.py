# доп - Ввести строку и образец,
# вывести на экран только слова
# начинающиеся и заканчивающиеся с заданного образца
string = input('Введите слова через пробел: ')
sample = input('Введите образец: ')
string = string.split(' ')
alf_consonants_en = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
alf_consonants_ru = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ'
answer = ''

for r in range(len(string)): #если мы считаем таб за 4 пробела, а не за отдельный символ
    if string[r]!= '\t' and string[r][0] == '\t':
        string[r] = string[r][1::]
        print(string[r][0])

for i in range(len(string)):
    if string[i]!= '' and string[i]!= '\t':
        if (string[i][0] in alf_consonants_en) or (string[i][0] in alf_consonants_ru) :
            answer = answer + string[i] + ' '
    #if string[i]== '\t' and *** - попытка обрабатывать слова, начинающиеся с таба - \tlkpsodhfioe
print('Слова начинающиеся с согласной:',answer)

sample_answer = ''
for k in range(len(string)):
    if string[k] != '' and string[k] != '\t':
        if string[k][0:len(sample)] == sample:
            sample_answer += string[k] + ' '
print('Слова начинающиеся с образца:', sample_answer)