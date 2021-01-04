import numpy as np
import matplotlib.pyplot as plt
from random import random #biblioteca para gerar numeros pseudo aleatorios
import matplotlib

matplotlib.rcParams.update({'font.size': 18})
plt.subplots_adjust(left=0.16, bottom=.13, right=.98, top=.95,
                wspace=None, hspace=None)

#vetor com o numero de interacoes
interacoes = np.logspace(0,6,100,base = 10.0, dtype = int)

#grafico de pi em funcao do numero de pontos gerados
fig1, ax1 = plt.subplots(figsize = [8,6]) 

#grafico desvio relativo em relacao ao valor de pi obtido usando o numpy
fig2, ax2 = plt.subplots(figsize = [8,6]) 

#valor esperado de pi
ax1.plot([.1,1e7],[np.pi,np.pi],'-',linewidth = 3,color = 'black')


for j in interacoes:
    #k é o número de pontos que obedecem a condicao x**2 + y**2 <= 1
    k = 0    
    fig, ax = plt.subplots(1,1,figsize = [8,8])
    for i in range(j): 
    
        #gera um número aleatório
        x = random()
        y = random()
        if x**2 + y**2 <= 1:
            k+= 1
            ax.plot(x,y,'s',markersize = 3,color = 'red')
        else:
            ax.plot(x,y,'o',markersize = 2,color = 'blue')
        
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Número de pontos gerados: ' + str(j))
    fig.savefig('inte/'+str(j)+'.png')
    pi = 4*k/j
    
    ax1.plot(j,pi,'s',color = 'red',markersize = 10)
    ax1.set_ylim([1.5,4.5])
    ax1.set_xlim([1,1e6])
    ax1.set_xscale('log')
    ax1.set_xlabel('Número de pontos gerados')
    ax1.set_ylabel('Valor de $\pi$')
    fig1.savefig('value/pi_value_'+str(j)+'.png')

    ax2.plot(j,100*abs((np.pi - pi)/np.pi),'o',color = 'red', markersize = 10)
    ax2.set_ylim([0.01,1e2])
    ax2.set_xlim([1,1e6])
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xlabel('Número de pontos gerados')
    ax2.set_ylabel('Desvio relativo do valor de $\pi$ (%)')    
    fig2.savefig('desvio/desvio_'+str(j)+'.png')

    
    
    l = j
#plt.show()
