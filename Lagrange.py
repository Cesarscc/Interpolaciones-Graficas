import sympy
import numpy as np
import matplotlib.pyplot as plt

def algoritmo(i, j):
    x_sim = sympy.symbols('x')
    return (x_sim-x[i]) / (x[j]-x[i]) if i != j else 1

def interpol_lagrange(x, y, num_puntos=100):
	
    x_sim = sympy.symbols('x')
    
    # Cantidad de puntos
    points = len(x)
    
    lj = []
    for k in range(points):
        lk = np.prod([algoritmo(i, k) for i in range(points)])
        lj.append(lk)

    #Lagrange
    pol = sum(y*lj)
    x_test = np.linspace(min(x), max(x), num_puntos)
    y_pol = [pol.subs(x_sim, i) for i in x_test]
    
    return x_test, y_pol

# Datos del problema
x = np.array([-3, -1, 2, 4])
y = np.array([0, 4 ,3 ,1])

#Puntos generados por lagrange
x_test, y_pol = interpol_lagrange(x, y)

# Mostrando lagrafica
plt.plot(x_test, y_pol)
plt.scatter(x, y)
plt.legend(['Lagrange', 'Datos'], loc='lower right')
plt.show()