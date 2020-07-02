import numpy as np 
from matplotlib import pyplot as plt 

# De no servir Scipy
try: 
    from scipy.special import comb, logsumexp
except ImportError:
    from scipy.misc import comb, logsumexp

def Polinomio_bernstein(i, n, t): 
    return comb(n, i) * (t**(n-i)) * (1 - t)**i 


def bezier_curve(points, numTimes=1000): 

    numPoints = len(points) 
    x = np.array([-3, -1, 2, 4])
    y = np.array([0, 4 ,3 ,1])

    t = np.linspace(0.0, 1.0, numTimes) 

    pol_array = np.array([ Polinomio_bernstein(i, numPoints-1, t) for i in range(0, numPoints) ]) 

    xvalues = np.dot(x, pol_array) 
    yvalues = np.dot(y, pol_array) 

    return xvalues, yvalues 


if __name__ == "__main__": 

    # Puntos
    numPoints = 4 
    points = np.random.rand(numPoints,2)*200 
    x = np.array([-3, -1, 2, 4])
    y = np.array([0, 4 ,3 ,1]) 

    # Mostrando la grafica
    xvalues, yvalues = bezier_curve(points, numTimes=1000) 
    plt.plot(xvalues, yvalues) 
    plt.plot(x, y, "ro") 
    for nr in range(len(points)): 
     plt.text(points[nr][0], points[nr][1], nr) 
    plt.legend(['Bezier', 'Datos'], loc='lower right')
    plt.show() 