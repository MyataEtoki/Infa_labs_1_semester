# ЛР 4
# 17.Реализовать модуль, содержащий функцию,
# находящую наименьшее общее кратное (НОК) двух чисел.
from least_common_multiple import l_c_m
number1, number2 = abs(int(input('Введите 1 число:'))), abs(int(input('Введите 2 число:')))
print(l_c_m(number1,number2))

