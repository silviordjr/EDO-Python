import numpy as np
import matplotlib.pyplot

popl = [27703,31498,36427,74166,90253,120980,170134,269415,409191,628241,796842,932748]
year = [1872,1890,1900,1920,1940,1950,1960,1970,1980,1991,2000,2010]

populacao_1910 = (popl[2] + popl[3])/2
print("A populacao ajustada de 1910:",populacao_1910) 

n = len(popl)    
m = len(year)
A = np.zeros((n,n), dtype=np.float64)
i = 0

while i < n:
    j = 0
    while j < n:
        A [i,j] = (year[i])**(n-(j+1))
        j = j + 1
    i = i + 1

coeficientes = np.linalg.solve(A, popl)
print("Os coeficientes do polinomio:\n",coeficientes)

populacao_ajuste = np.array([])
i = 0
while i < n:
    pop_ajuste = 0
    m = len(year)
    while m > 0:
        pop_ajuste = pop_ajuste + coeficientes[n-m]*year[i]**(m-1)
        m = m -1
    pop_ajuste_lista = np.array([pop_ajuste])
    populacao_ajuste = np.concatenate((populacao_ajuste,pop_ajuste_lista))
    i = i + 1

n = len(popl)    
m = len(year)
ano_estimativa = 1910
pop_estimativa = 0

while m > 0:
    pop_estimativa = pop_estimativa + coeficientes[n-m]*ano_estimativa**(m - 1)
    m = m -1 

print("Pelo polinimio, a populacao de 1910:",pop_estimativa)

n = len(popl)    
m = len(year)
ano_estimativa = 2021
pop_estimativa = 0

while m > 0:
    pop_estimativa = pop_estimativa + coeficientes[n-m]*ano_estimativa**(m - 1)
    m = m -1 

print("A populacao estimada para o ano de",ano_estimativa,":",pop_estimativa)


x = np.array([ano_estimativa])
y = np.array([pop_estimativa])
ano_ajuste = np.copy(year)
ano_ajuste = np.concatenate((ano_ajuste,x))
populacao_ajuste = np.concatenate((populacao_ajuste,y))

matplotlib.pyplot.plot(year, popl, linestyle='--', marker='o', color = 'green', markersize = 4)
matplotlib.pyplot.plot(ano_ajuste, populacao_ajuste, linestyle='--', marker='o', color = 'purple', markersize = 4)
matplotlib.pyplot.title('Crescimento populacional')
matplotlib.pyplot.xlabel('Ano')
matplotlib.pyplot.ylabel('População')
matplotlib.pyplot.legend(['Curva de Crescimento Populacional','Curva da Estimativa'], fontsize=14)
axes = matplotlib.pyplot.gca()
axes.yaxis.grid(b=True, color='black', alpha=0.3, linestyle='-.', linewidth=1)
matplotlib.pyplot.figure(figsize=(10.5, 9))
matplotlib.pyplot.show()





