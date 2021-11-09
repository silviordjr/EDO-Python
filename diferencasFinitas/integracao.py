import numpy as np
import math 

a = 0 #Intervalos
b = 5
n = 10 #Numero de intervalos na regra composta; Obs.: n deve ser par


#definindo a entrada
def f(x): #Funçaõ de escolha
    return  5*x**2 + 8*x + 1
def g(x):
    return x**2 + x

#Trapézio Composto
def trapezioCompostoF(f,a,b,n): #Função F(x)
    x = np.linspace(a, b, num=n) #Definindo x; ira variar de a até b em n intervalos
    y = f(x) #chamando a função
    dx = x[1] - x[0] #definindo o tamanho do initervalo
    integral_composto_f = 0 #Inicio do processo iterativo (I = valor de integral)
    integral_composto_f += dx*y[0]/2 #somando primeiro trapezio
    for i in range(1,x.size-1): #somando demais trapezios
        integral_composto_f += dx*y[i]
    integral_composto_f += dx*y[-1]/2 #somando ultimo trapezio
    return integral_composto_f

def trapezioCompostoG(g,a,b,n): #Função G(x)
    x = np.linspace(a, b, num=n) #Definindo x; ira variar de a até b em n intervalos
    y = g(x) #chamando a função
    dx = x[1] - x[0] #definindo o tamanho do initervalo
    integral_composto_g = 0 #Inicio do processo iterativo (I = valor de integral)
    integral_composto_g += dx*y[0]/2 #somando primeiro trapezio
    for i in range(1,x.size-1): #somando demais trapezios
        integral_composto_g += dx*y[i]
    integral_composto_g += dx*y[-1]/2 #somando ultimo trapezio
    return integral_composto_g

#Simpson
def simpsonF(f,a,b,n): #Função F(X)
    if n % 2 != 0 or n<1:
        raise ValueError("n deve ser par e maior que 1")
    h = (b - a)/n
    soma_impar = 0
    soma_par = 0
    for k in range (1,n,2): #Pontos de ordem impar
        soma_impar = soma_impar + f(a+k*h)
    for k in range (2,n,2): #Pontos de ordem par
        soma_par = soma_par + f(a+k*h)
    return (h/3)*(f(a) + 4*soma_impar + 2*soma_par + f(b))

def simpsonG(g,a,b,n): #Função G(X)
    if n % 2 != 0 or n<1:
        raise ValueError("n deve ser par e maior que 1")
    h = (b - a)/n
    soma_impar = 0
    soma_par = 0
    for k in range (1,n,2): #Pontos de ordem impar
        soma_impar = soma_impar + g(a+k*h)
    for k in range (2,n,2): #Pontos de ordem par
        soma_par = soma_par + g(a+k*h)
    return (h/3)*(g(a) + 4*soma_impar + 2*soma_par + g(b))

integral_simpson_f = simpsonF(f,a,b,n)
print("A integral de F(X) pelo método de Simpson:",integral_simpson_f)
integral_simpson_g = simpsonG(g,a,b,n)
print("A integral de G(X) pelo método de Simpson:",integral_simpson_g)
integral_trapézio_composto_f = trapezioCompostoF(f,a,b,n)
print("A Integral de F(x) por trapezio composto:",integral_trapézio_composto_f)
integral_trapézio_composto_g = trapezioCompostoG(g,a,b,n)
print("A Integral de G(x) por trapezio composto:",integral_trapézio_composto_g)
