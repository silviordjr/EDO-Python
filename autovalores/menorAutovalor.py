import numpy as np
import math

A = np.array([[1, 2],[2,3]])
AI = np.linalg.inv(A)
x = np.array([1,1])
xt = x.T
aux = xt.dot(AI)
aux2 = AI.dot(x)
norma = np.linalg.norm(aux2)
autovalor = aux.dot(x)
listaAux = [autovalor]
erro = 1

while erro > 10**(-4):
    x = (AI.dot(x))/norma
    norma = np.linalg.norm(x)
    xt = x.T
    aux = xt.dot(AI)
    autovalor = aux.dot(x)/(xt.dot(x))
    listaAux.append(autovalor)
    erro = math.fabs((listaAux[-2]-listaAux[-1])/listaAux[-1])

autovalorMenor = 1/autovalor

print(autovalorMenor)
