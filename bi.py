import numpy as np
import matplotlib.pyplot as plt

def map(r, x):
    N = 700
    for i in range(N):
        x = r*x*(1-x)
    return(x)


y = np.linspace(.1, 3, 100)
r = np.linspace(-2, 4, 9000)
#for x in y:
#    plt.plot(r, map(r,x), 'b.')
plt.plot(r, map(r, .1), 'b.')
plt.ylim(-.5, 1.5)
plt.xlim(-2, 4)
plt.xlabel('r')
plt.ylabel(r'$x_{700}$')
plt.title(r'$x_{n+1} = r\cdot x_n\cdot(1-x_n)$; $x_0=.1$')
plt.show()
