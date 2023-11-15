# ЛР 4
# 17.Реализовать модуль, содержащий функцию,
# находящую наименьшее общее кратное (НОК) двух чисел.
# ДОП - можно находить НОД и НОК для более чем двух чисел.
from least_common_multiple import l_c_m, g_c_d
#number1, number2 = abs(int(input('Введите 1 число:'))), abs(int(input('Введите 2 число:')))
#print(l_c_m(number1,number2))
numbers = [abs(int(x)) for x in input('Введите числа через пробел:').split()]
gcds = [0] * (len(numbers))
gcds[0] = numbers[0]
lcms = [0]*(len(numbers))
lcms[0] = numbers[0]
for i in range(len(numbers)-1):
    gcds[i+1] = g_c_d(gcds[i],numbers[i+1])
for i in range(len(numbers)-1):
    lcms[i+1] = l_c_m(lcms[i],numbers[i+1])
print('НОД введённых чисел',gcds[-1])
print('НОК введённых чисел',lcms[-1])

