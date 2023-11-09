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