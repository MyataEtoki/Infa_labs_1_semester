number = False
answer = ''
while number == False:
    B = input('Введите число: ')
    try:
        A = int(B)
        number = True
        if A<0:
            number = False
    except ValueError:
        number = False
        print('Это не число!')


while A > 0:
    answer = str(A % 8) + answer
    A = A // 8
print('Ваше число в восьмеричной СС:', answer)