def l_c_m(a,b): # НОК
    m = a * b
    return m // g_c_d(a,b) # a+b - НОД
def g_c_d(a,b): #O(log(min(a,b)))
    #greatest common divisor - НОД
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b


#НОК для 3 чисел - пояснение для кода в main файле, не используется
def l_c_m_more(a,b,c): # НОК 3+ чисел
    return l_c_m(l_c_m(a,b),c) # Берём НОК предыдущих двух чисел и находим его НОК с следующим числом