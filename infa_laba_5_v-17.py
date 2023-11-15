# ЛР 5
# 17. Задание 1 - 1.	Задав две матрицы A[M, N] и B[M, N],
# выполните сложение и вычитание матриц,
# чтобы вычислить результирующие матрицы C[M, N] и D[M, N].
'''
a=int(input('Введите количество строк в матрицах A и B:'))
A=[]
B=[]

print('Введите матрицу A по-строчно, разделяя эл-ты пробелом(или таб-ом)')
for i in range(a):
    A.append(list(map(int, input().split())))

print('Введите матрицу B по-строчно, разделяя эл-ты пробелом(или таб-ом)')
for i in range(a):
    B.append(list(map(int, input().split())))
'''
#Образцовые матрицы 1
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[8,8,2],[4,7,2],[8,2,5]]

k=len(A)
def sum_AB(a,b):
    C = [[0] * k for i in range(k)]
    for m in range(len(a)):
        for n in range(len(a[m])):
            C[m][n] = a[m][n]+b[m][n]
    return C

def difference_AB(a,b):
    D = [[0] * k for i in range(k)]
    for m in range(len(a)):
        for n in range(len(a[m])):
            D[m][n] = a[m][n]-b[m][n]
    return D

# 2 задание - 2.	Реализуйте функцию, которая перемножает
# две матрицы A[M, N] и B[N, P] для получения
# результирующей матрицы E[M, P]. Вывести результат на экран.
'''
a2=int(input('Введите количество строк в матрице A2:'))
b2=int(input('Введите количество строк в матрице B2:'))
A2=[]
B2=[]

print('Введите матрицу A2 по-строчно, разделяя эл-ты пробелом')
for i in range(a2):
    A2.append(list(map(int, input().split())))

print('Введите матрицу B2 по-строчно, разделяя эл-ты пробелом')
for i in range(b2):
    B2.append(list(map(int, input().split())))
'''
#Образцовые матрицы 2
A2 = [[-2,3,0],[3,-1,1]]
# -2 3 0
# 3 -1 1
B2 = [[-1,2],[0,-3],[2,1]]
# -1 2
# 0 -3
# 2 1

def product_AB(a,b):
    E = [[0] * len(A2) for r in range(len(A2))]
    for m in range(len(A2)):
        for n in range(len(b[0])):
            E[m][n] = sum(A2[m][t]*B2[t][n] for t in range(len(b)))
    return E

print('Сумма матриц А и В:',sum_AB(A,B))
print('Разность матриц А и В:',difference_AB(A,B))
print('Произведение матрицы А2 на В2:',product_AB(A2,B2))