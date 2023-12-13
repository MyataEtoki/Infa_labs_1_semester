def decimal_to_octal_negative(decimal):

    # Переводим отрицательное число в дополнительный код
    complement = bin(decimal & 0xffffffff)[2:]
    print(complement)
    # Добавляем нули в начало до достижения длины кратной 3
    complement = complement.zfill((len(complement) + 2) // 3 * 3)
    print(complement)
    # Группируем биты по три и переводим их в восьмеричную систему
    octal_digits = [complement[i:i+3] for i in range(0, len(complement), 3)]
    octal = ''.join(str(int(group, 2)) for group in octal_digits)
    print(octal_digits)
    return octal

# Пример использования
negative_decimal = -23
octal_representation = decimal_to_octal_negative(negative_decimal)
print(f"Отрицательное число {negative_decimal} в восьмеричной системе: {octal_representation}")