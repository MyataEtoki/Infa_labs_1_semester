number_input = False
answer = ''
number = 0
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
    ans = bin(number+(1<<8))[2:]
    # dop_code = bin(abs(number))[2:]
    # obr_code = ''
    # mask = (1 << 32) - 1
    # for i in range(len(dop_code)):
    #     if dop_code[i] == '0':
    #         obr_code += '1'
    #     else:
    #         obr_code += '0'
    # print(obr_code, dop_code)
    print(ans)
    # print('Ваше число в восьмеричной СС:', ans)