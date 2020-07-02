import numpy as np
from scipy import interpolate

import matplotlib.pyplot as plt

# Datos
lista =np.array( [(-1,0), (1, 4), (3, -2), (4,3), (6,1)])
x=lista[:,0]
y=lista[:,1]


tam=len(x)  

t=np.linspace(0,1,tam-2,endpoint=True)
t=np.append([0,0,0],t)
t=np.append(t,[1,1,1])

aux=[t,[x,y],3]
auxinterp=np.linspace(0,1,(max(tam*2,1000)),endpoint=True)
oput = interpolate.splev(auxinterp,aux)

plt.plot(x,y,'k--',label='Puntos de Control',marker='o',markerfacecolor='orange')
plt.plot(oput[0],oput[1],'b',linewidth=1.5,label='B-Spline Curva')
plt.legend(loc='lower right')
plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
plt.title('Curva B-Spline Cubica')
plt.show()

