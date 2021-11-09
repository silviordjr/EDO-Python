import numpy as np

A = np.array([[2,1,2],[1,2,1],[2,1,2]])

n = A.shape[0]
assert A.shape[1] == n
p = np.array([1.])
Ak = np.array(A)
for k in range(1, n + 1):
    pk = -Ak.trace() / k
    p = np.append(p, pk)
    Ak += np.diag(np.repeat(pk, n))
    Ak = np.dot(A, Ak)

print ('Os coeficientes do polinômio característico são:', p)
