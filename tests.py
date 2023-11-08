print(54%24)





'''def find_div(n):
    a = []
    for j in range(1, int(n ** 0.5) + 1):
        if (n % j == 0):
            a.append(j)
            if (j != n // j):
                a.append(n // j)
    a.sort()
    return a

number1, number2 = int(input()), int(input())
if number1 < number2:  # а что если они равны?
    div1, div2 = find_div(number2), find_div(number1)
else:
    div1, div2 = find_div(number1), find_div(number2)

divs = []
for i in range(len(div1)):
    if div1[i] in div2:
        divs.append()
'''