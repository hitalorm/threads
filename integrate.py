import numpy as np
import matplotlib.pyplot as plt
from random import random
from scipy.integrate import quad    
import matplotlib
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)


#função que vamos utilizar
def f(x):
    y = np.sin(x**3)+x**2
    return y

#estimador de números aleatorios
def estimator(x_min, x_max):
    x_i = x_min + random()*(x_max - x_min)
    y_i = f(x_i)
    
    return x_i,y_i

#intervalo da integral
x_min = 0
x_max = 3

#integral usando numpy
res, err = quad(f, 0, 3)

#-----------------------------------------------------------------------
#plotando só a função com a área do retângulo
#-----------------------------------------------------------------------

#vetores para plotar a função
x = np.linspace(x_min,x_max,100)
y = f(x)

fig,ax = plt.subplots(1,1,figsize = [7,5])
matplotlib.rcParams.update({'font.size': 15})
plt.subplots_adjust(left=0.16, bottom=.13, right=.98, top=.95,
                wspace=None, hspace=None)

ax.plot(x,y)



#estimando um valor para x_i e calculando f(x_i)
x_i,y_i = estimator(x_min,x_max)
sub= y_i*(x_max-x_min) #area do retangulo
    
ax.plot(x_i,y_i,'s', color = 'red')
ax.plot([x_i,x_i],[0,y_i],'-',color ='red')
ax.fill_between([x_min,x_max], [y_i,y_i], color = 'gray', alpha = 0.2)
ax.text(x_i,0,'x1',color = 'red',horizontalalignment='center',
         verticalalignment='top')
ax.text(x_i,y_i+1,'f(x1)',color = 'red',horizontalalignment='center',
         verticalalignment='top')

ax.tick_params(axis='both', which = 'major', length = 10,width = 2, direction = 'in')
ax.tick_params(axis='both', which = 'minor', length = 6,width = 1, direction = 'in')
ax.set_xlim([0,3])
ax.set_ylim([0,10])
ax.set_xlabel('x', fontsize = 15)
ax.set_ylabel('y', fontsize = 15)
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_major_locator(MultipleLocator(1))
plt.show()

#-----------------------------------------------------------------------
#Calculando a integral depois de N interações
#-----------------------------------------------------------------------
sub = 0
sub2= 0
for i in range(100000):
    #estimando um valor para x_i e calculando f(x_i)
    x_i,y_i = estimator(x_min,x_max)

    #calculando a area do retangulo
    sub+= y_i*(x_max-x_min)
    
    #média dos retângulos
    q = sub/(i+1)
    
    #calculando o desvio padrão
    sub2+= (y_i*(x_max-x_min))**2
    q2 = sub2/(i+1)
    std = (q2-q**2)/(i+1)
    std = np.sqrt(std)

    desvio = 100*abs(res-q)/res
    #condição de que se o desvio relativo for menor que 0,0001% para o for
    if desvio < 0.0001:
        break

print("integral é: " + '{0:.2f}'.format(q))
print("desvio padrão é: " + '{0:.2f}'.format(std))
print("foram necessárias " + str(i) + " interações")


