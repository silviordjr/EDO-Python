from __future__ import division
import math
import numpy as np
import time
from numpy import linalg 

n = 100
s = 10**6 #valor lido na tabela
f = 10**4 #valor lido na tabela
iteracoes = 10**5
tolerancia = 10**(-7)
k = s * n #valor lda rigidez de cada mola
# Vetor b das constantes
b = np.zeros(n)
b[n-1] = f

print('Dados da simulacao: numero de molas:',n,"Rigidez:",s,"Forca:",f,"\nIteracoes maxima:",iteracoes,"Tolerancia:",tolerancia)

#Matriz A dos coeficientes
matriz = np.zeros((n,n), dtype=np.float64) #Criando matriz quadrada do tamanho proposto
i = 0 #Auxiliar para a criacao da matriz A dos coeficientes
while i < n:
    j = 0 #Auxiliar para a criacao da matriz A dos coeficientes
    while j < n:
        if i == j: #Construção da matriz A dos coeficiente; como K= cte: 
            matriz [i,j] = 2*k
            if i != n-1: #Verificando tamanho da matriz
                matriz [i, j + 1] = -k
            if i != 0: #Verificando tamanho da matriz
                matriz [i,j - 1] = -k
        j = j + 1
    i = i + 1

#Soluçaõ por algoritmo nativo
ini = time.time() #inicio da contagem de tempo
solucao = np.linalg.solve (matriz,b)
fim = time.time()

print("A solucao por algoritmo nativo:", solucao, "no tempo de",fim-ini)

#Numeros de condicionamento
norma1 = np.linalg.cond(matriz,p=1)
norma_infinito = np.linalg.cond(matriz,p=2) 
nroma2 = np.linalg.cond(matriz,p=np.inf)

print("Numero de Condicionamento 1:",norma1,"Numero de Condicionamento Infinito:",norma_infinito,"Numero de Condicionamento 2:",nroma2)



print("A matriz A dos coeficientes:\n",matriz,"\nO vetor b de constantes:",b)
determinante = np.linalg.det(matriz) #CalcuLo do determinante da matriz (verificar se o sistema e consistente)
if determinante != 0:
    print("O determinante da matriz e:",determinante,"Portanto, o sistema e consistente.")
else:
    print("O sistema e inconsistente.")
posto = np.linalg.matrix_rank(matriz)#CalcuLo do determinante da matriz (verificar se o sistema e determinado)
if posto != 0:
    print("O posto da matriz e:",posto,"Portanto, o sistema e determinado.")
else:
    print("O sistema é indeterminado.")

#Gauss Seidel
ini = time.time() #inicio da contagem de tempo
x0 = np.ones(n) #ultima solucap
x = np.copy(x0) #solucao atual
it = 0  
iteracoes  
while (it < iteracoes):     
    it = it+1  
    #iteracao de Jacobi 
    for i in np.arange(n):  
        x[i] = b[i]  
        for j in np.concatenate((np.arange(0,i),np.arange(i+1,n))):  
            x[i] -= matriz[i,j]*x[j]  
        x[i] /= matriz[i,i]  
       
    #tolerancia  
    if (np.linalg.norm(x-x0,np.inf) < tolerancia):  
        break
    #prepara nova iteracao  
    x0 = np.copy(x)  
fim = time.time() #fim da contagem de tempo
print ("Gauss Seidel:")
print ("O vetor solucao:",x)
print('O numero de iteracoes:',it)
print('Erro:',(np.linalg.norm(x-x0,np.inf)))
print('Tempo de execucao:',fim-ini)


#Gauss Jacobi
ini = time.time() #inicio da contagem de tempo
x0 = np.ones(n) #ultima solucao
x = np.zeros(n)  #solucao atual
it = 0  
iteracoes  
while (it < iteracoes):  
    it = it+1  
    #iteracao de Jacobi 
    for i in np.arange(n):  
        x[i] = b[i]  
        for j in np.concatenate((np.arange(0,i),np.arange(i+1,n))):  
            x[i] -= matriz[i,j]*x0[j]  
        x[i] /= matriz[i,i]  
    #tolerancia  
    if (np.linalg.norm(x-x0,np.inf) < tolerancia):  
        break 
    #prepara nova iteracao  
    x0 = np.copy(x)  

fim = time.time() #fim da contagem de tempo
print('Gauss Jacobi:')
print ("O vetor solucao:",x)
print('O numero de iteracoes:',it)
print('Erro:',(np.linalg.norm(x-x0,np.inf)))
print('Tempo de execucao:',fim-ini)
