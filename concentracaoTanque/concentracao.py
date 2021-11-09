import numpy as np
import matplotlib.pyplot

#informações do problema
constante1 = 1000 #(k1/k2)
constante2 = 2 #(k3/k2)
passo = 0.001 #passo do sistema
x1_0 = 1 #Condições de contorno (exercício)
x2_0 = 0 #Condições de contorno (exercício)
tempoInicial = 0
tempoFinal = 0.015


#construindo o vetor de tempo
tempo = [tempoInicial]
i = 0

while (tempo[i] < tempoFinal):
    tempoInicial = tempoInicial + passo
    tempo.append(tempoInicial)

    i = i + 1

#definindo equação das derivadas
def variacaoX1(constante1, x1, x2):
    return ((-constante1*x1) + x2)

def variacaoX2(constante1, constante2, x1, x2):
    return((constante1*x1)-((1 + constante2)*x2))

#definindo os vetores dos resultados
vetor_x1 = np.zeros(len(tempo))
vetor_x2 = np.zeros(len(tempo))

vetor_x1[0] = x1_0
vetor_x2[0] = x2_0

#construindo vetores de resultado
i = 1

while (i < len(vetor_x1)):

    primeiroPontoX1 = variacaoX1(constante1, vetor_x1[i - 1], vetor_x2[i - 1])
    aux1 = vetor_x1[i - 1] + 0.5*primeiroPontoX1*passo
    aux2 = vetor_x2[i - 1] + 0.5*passo
    segundoPontoX1 = variacaoX1(constante1, aux1, aux2)
    x1 = vetor_x1[i - 1] + segundoPontoX1*passo
    vetor_x1[i] = x1

    primeiroPontoX2 = variacaoX2(constante1, constante2, vetor_x1[i - 1], vetor_x2[i - 1])
    aux3 = vetor_x1[i - 1] + 0.5*passo
    aux4 = vetor_x2[i - 1] + 0.5*passo*primeiroPontoX2
    segundoPontoX2 = variacaoX2(constante1, constante2, aux3, aux4)
    x2 = vetor_x2[i - 1] + 0.5*segundoPontoX2*passo
    vetor_x2[i] = x2

    i = i + 1

print("Vetor 1 com passo = 0,001:\n",vetor_x1)
print("Vetor 2 com passo = 0,001:\n",vetor_x2)

matplotlib.pyplot.plot(tempo, vetor_x1, linestyle='--', marker='o', color = 'blue', markersize = 4, label="Variação da concentração de A")  
matplotlib.pyplot.plot(tempo, vetor_x2, linestyle='--', marker='o', color = 'red', markersize = 4, label="Variação da concentração de B")  
matplotlib.pyplot.title('Concentração x Tempo - passo = 0,001')
matplotlib.pyplot.legend()
matplotlib.pyplot.xlabel('Tempo (s)')
matplotlib.pyplot.ylabel('Concentração (adimensional)')
axes = matplotlib.pyplot.gca()
axes.yaxis.grid(b=True, color='black', alpha=0.3, linestyle='-.', linewidth=1)
matplotlib.pyplot.show()

#mudando o passo
passo = 0.0005 #passo do sistema

#definindo os vetores dos resultados
vetor_x1 = np.zeros(len(tempo))
vetor_x2 = np.zeros(len(tempo))

vetor_x1[0] = x1_0
vetor_x2[0] = x2_0

#construindo vetores de resultado
i = 1

while (i < len(vetor_x1)):

    primeiroPontoX1 = variacaoX1(constante1, vetor_x1[i - 1], vetor_x2[i - 1])
    aux1 = vetor_x1[i - 1] + 0.5*primeiroPontoX1*passo
    aux2 = vetor_x2[i - 1] + 0.5*passo
    segundoPontoX1 = variacaoX1(constante1, aux1, aux2)
    x1 = vetor_x1[i - 1] + segundoPontoX1*passo
    vetor_x1[i] = x1

    primeiroPontoX2 = variacaoX2(constante1, constante2, vetor_x1[i - 1], vetor_x2[i - 1])
    aux3 = vetor_x1[i - 1] + 0.5*passo
    aux4 = vetor_x2[i - 1] + 0.5*passo*primeiroPontoX2
    segundoPontoX2 = variacaoX2(constante1, constante2, aux3, aux4)
    x2 = vetor_x2[i - 1] + 0.75*segundoPontoX2*passo
    vetor_x2[i] = x2

    i = i + 1

print("Vetor 1 com passo = 0,0005:\n",vetor_x1)
print("Vetor 2 com passo = 0,0005:\n",vetor_x2)

matplotlib.pyplot.plot(tempo, vetor_x1, linestyle='--', marker='o', color = 'blue', markersize = 4, label="Variação da concentração de A")  
matplotlib.pyplot.plot(tempo, vetor_x2, linestyle='--', marker='o', color = 'red', markersize = 4, label="Variação da concentração de B")  
matplotlib.pyplot.title('Concentração x Tempo - passo = 0,0005')
matplotlib.pyplot.legend()
matplotlib.pyplot.xlabel('Tempo (s)')
matplotlib.pyplot.ylabel('Concentração (adimensional)')
axes = matplotlib.pyplot.gca()
axes.yaxis.grid(b=True, color='black', alpha=0.3, linestyle='-.', linewidth=1)
matplotlib.pyplot.show()


















