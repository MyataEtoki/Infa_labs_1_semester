#17. Задание 1 - 1.	Задав две матрицы A[M, N] и B[M, N],
# выполните сложение и вычитание матриц,
# чтобы вычислить результирующие матрицы C[M, N] и D[M, N].
k=3
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[8,8,2],
     [4,7,2],
     [8,2,5]]

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
A2 = [[-2,3,0],
      [3,-1,1]]

B2 = [[-1,2],
      [0,-3],
      [2,1]]

def product_AB(a,b):
    E = [[0] * len(A2) for r in range(len(A2))]
    for m in range(len(A2)):
        for n in range(len(b[0])):
            E[m][n] = sum(A2[m][t]*B2[t][n] for t in range(len(b)))
    return E

print(sum_AB(A,B))
print(difference_AB(A,B))
print(product_AB(A2,B2))