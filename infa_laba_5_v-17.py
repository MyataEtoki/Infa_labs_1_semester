A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[8,8,2],[4,7,2],[8,2,5]]
k=3
def sum_AB(a,b):
    C = [[0] * k for i in range(k)]
    for m in range(len(a)):
        for n in range(len(a[m])):
            C[m][n] = a[m][n]+b[m][n]
    return C

def minus_AB(a,b):
    D = [[0] * k for i in range(k)]
    for m in range(len(a)):
        for n in range(len(a[m])):
            D[m][n] = a[m][n]-b[m][n]
    return D

print(sum_AB(A,B))