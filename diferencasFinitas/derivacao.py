import math 

def f(x):
    return x**2 

def g(x):
    return 3*x/(5*x**2 - 2*x + 1)

a = 4
h = 0.1

def MDF_centrada_f(f,a,h):
    return (f(a+h) - f(a-h))/(2*h)

def MDF_centrada_g(g,a,h):
    return (g(a+h) - g(a-h))/(2*h)

def MDF_atrasada_f(f,a,h):
    return -1*(f(a)-4*f(a-h)+3*f(a-2*h))/(2*h)

def MDF_atrasada_g(g,a,h):
    return -1*(g(a)-4*g(a-h)+3*g(a-2*h))/(2*h)

def MDF_adiantada_f(f,a,h):
    return (-3*f(a)+4*f(a+h)-f(a+2*h))/(2*h)

def MDF_adiantada_g(g,a,h):
    return (-3*g(a)+4*g(a+h)-g(a+2*h))/(2*h)

diff_centrada_f = MDF_centrada_f(f,a,h)
print("A derivada de F(x) no ponto",a,"pelo metodo de diferencas finitas centradas:",diff_centrada_f)
diff_centrada_g = MDF_centrada_g(g,a,h)
print("A derivada de G(x) no ponto",a,"pelo metodo de diferencas finitas centradas:",diff_centrada_g)
diff_atrasada_f = MDF_atrasada_f(f,a,h)
print("A derivada de F(x) no ponto",a,"pelo metodo de diferencas finitas atrasadas",diff_atrasada_f)
diff_atrasada_g = MDF_atrasada_g(g,a,h)
print("A derivada de G(x) no ponto",a,"pelo metodo de diferencas finitas atrasadas",diff_atrasada_g)
diff_adiantada_f = MDF_adiantada_f(f,a,h)
print("A derivada de F(x) no ponto",a,"pelo metodo de diferencas finitas adiantadas",diff_adiantada_f)
diff_adiantada_g = MDF_adiantada_g(g,a,h)
print("A derivada de G(x) no ponto",a,"pelo metodo de diferencas finitas adiantadas",diff_adiantada_g)
