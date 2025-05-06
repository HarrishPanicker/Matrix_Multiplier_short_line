def array_mult(A, B):
    return [[sum((A[i][k] * B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))] 
