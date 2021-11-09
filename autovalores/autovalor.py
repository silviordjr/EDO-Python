import numpy as np
import math

A = np.array([[3, 1, 3, 1],[1, 3, 1, 3],[3, 1, 2, 2],[1, 3, 2, 2]])
x = np.array([1,1,1,1])
xt = x.T
aux = xt.dot(A)
aux2 = A.dot(x)
norma = np.linalg.norm(aux2)
autovalor = aux.dot(x)
listaAux = [autovalor]
erro = 1

while erro > 10**(-4):
    x = (A.dot(x))/norma
    norma = np.linalg.norm(x)
    xt = x.T
    aux = xt.dot(A)
    autovalor = aux.dot(x)/(xt.dot(x))
    listaAux.append(autovalor)
    erro = math.fabs((listaAux[-2]-listaAux[-1])/listaAux[-1])

print(autovalor)





