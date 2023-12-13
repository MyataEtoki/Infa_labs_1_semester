number_input = False
answer = ''
while number_input == False:
    B = input('Введите число: ')
    try:
        number = int(B)
        number_input = True
    except ValueError:
        number_input = False
        print('Это не число!')

if number >= 0:
    while number > 0:
        answer = str(number % 8) + answer
        number = number // 8
    print('Ваше число в восьмеричной СС:', answer)
else:
    complement = bin(number & 0xffffffff)[2:]
    # Добавляем нули в начало до достижения длины кратной 3
    complement = complement.zfill((len(complement) + 2) // 3 * 3)
    # Группируем биты по три и переводим их в восьмеричную систему
    octal_digits = [complement[i:i+3] for i in range(0, len(complement), 3)]
    octal = ''.join(str(int(group, 2)) for group in octal_digits)

    print('Ваше число в восьмеричной СС:', octal)