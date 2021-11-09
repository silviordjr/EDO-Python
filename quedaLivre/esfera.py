import numpy as np
import math 
import matplotlib.pyplot

y0 = 4.5 #Posicão inicial do centro da esfera (metros)
v0 = (-0.5) #Velocidade inicial da esfera (para cima; m/s)
r = 0.1 #Raio da esfera (metros)
m = 1 #Massa da esfera (kg)
k = 10**4 #Constante de rigidez (N/m)
ts = 15 #Tempo final para simulação (s)
dt = 0.0011 #Passo de tempo (s)
g = (-9.81) #Aceleração da gravidade (m/s2)

def aceleracaoQueda(g):
    return g

def aceleracaoImpacto(g,k,delta,m):
    return (k/m)*delta + g


#Construindo vetor de tempo
ti = 0
tempo = [ti]
i = 0

while tempo[i] < ts:
    ti = ti + dt
    tempo.append(ti)
    i = i + 1

if tempo[-1] >= ts:
    del(tempo[-1])
    tempo.append(ts)

posicao = np.zeros(len(tempo))
posicao[0] = y0
velocidade = np.zeros(len(tempo))
velocidade[0] = v0
aceleracao = np.zeros(len(tempo))
aceleracao[0] = g
i = 1
delta = r - posicao[0]

while i < len(tempo):
    if delta < 0:
        ac = aceleracaoQueda(g)
        aceleracao[i] = ac
        velocidade[i] = velocidade[i-1] + aceleracao[i]*dt
        posicao[i] = posicao[i-1] + velocidade[i]*dt
    
    else:
        ac = aceleracaoImpacto(g,k,delta,m)
        aceleracao[i] = ac
        velocidade[i] = velocidade[i-1] + aceleracao[i]*dt
        posicao[i] = posicao[i-1] + velocidade[i]*dt

    delta = r - posicao[i]
    i = i + 1

v_max = np.max(velocidade)
v_max_teoria = - math.sqrt(v0**2 + 2*g*(r-y0))
pos_max = np.max(posicao)
ac_max = np.max(aceleracao)

print("Vetor de tempo:",tempo)
print("Vetor de velocidade:",velocidade)
print("Vetor de posicao:",posicao)
print("Vetor de aceleracao:",aceleracao)
print("A velocidade maxima encontrada:",v_max,"Enquanto a velocidade maxima na teoria:",v_max_teoria,"Representando um erro de:",(v_max-v_max_teoria)/v_max_teoria,"%\nA aceleracao maxima:",ac_max,"a posicao maxima:",pos_max)

matplotlib.pyplot.plot(tempo, posicao, linestyle='--', marker='o', color = 'black', markersize = 4)  
matplotlib.pyplot.title('Posição x Tempo')
matplotlib.pyplot.xlabel('Tempo (s)')
matplotlib.pyplot.ylabel('Altura do centro (m)')
axes = matplotlib.pyplot.gca()
axes.yaxis.grid(b=True, color='black', alpha=0.3, linestyle='-.', linewidth=1)
matplotlib.pyplot.show()

matplotlib.pyplot.plot(tempo, velocidade, linestyle='--', marker='o', color = 'black', markersize = 4)  
matplotlib.pyplot.title('Velocidade x Tempo')
matplotlib.pyplot.xlabel('Tempo (s)')
matplotlib.pyplot.ylabel('Velocidade (m/s)')
axes = matplotlib.pyplot.gca()
axes.yaxis.grid(b=True, color='black', alpha=0.3, linestyle='-.', linewidth=1)
matplotlib.pyplot.show()

matplotlib.pyplot.plot(tempo, aceleracao, linestyle='--', marker='o', color = 'black', markersize = 4)  
matplotlib.pyplot.title('Aceleração x Tempo')
matplotlib.pyplot.xlabel('Tempo (s)')
matplotlib.pyplot.ylabel('Aceleração (m/s²)')
axes = matplotlib.pyplot.gca()
axes.yaxis.grid(b=True, color='black', alpha=0.3, linestyle='-.', linewidth=1)
matplotlib.pyplot.show()


