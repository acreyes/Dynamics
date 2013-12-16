#Author: Adam Reyes
#RK4 solution to Rossler Attractor
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
##########LOCAL FUNCTIONS##########
def dxdt(x, y, z, a, b, c):
    return(-y - z)
def dydt(x, y, z, a, b, c):
    return(x + a*y)
def dzdt(x, y, z, a, b, c):
    return(b + z*(x-c))
def D(x, y, z, sig, rho, beta, dim):
    if(dim == 0):
        return(dxdt(x, y, z, sig, rho, beta))
    elif(dim == 1):
        return(dydt(x, y, z, sig, rho, beta))
    elif(dim == 2):
        return(dzdt(x, y, z, sig, rho, beta))
def rk4(x, y, z, dt, sig, rho, beta):
    kx1 = dt*D(x, y, z, sig, rho, beta, 0)
    ky1 = dt*D(x, y, z, sig, rho, beta, 1)
    kz1 = dt*D(x, y, z, sig, rho, beta, 2)

    kx2 = dt*D(x+.5*kx1, y+.5*ky1, z+.5*kz1, sig, rho, beta, 0) 
    ky2 = dt*D(x+.5*kx1, y+.5*ky1, z+.5*kz1, sig, rho, beta, 1)
    kz2 = dt*D(x+.5*kx1, y+.5*ky1, z+.5*kz1, sig, rho, beta, 2)

    kx3 = dt*D(x+.5*kx2, y+.5*ky2, z+.5*kz2, sig, rho, beta, 0)
    ky3 = dt*D(x+.5*kx2, y+.5*ky2, z+.5*kz2, sig, rho, beta, 1)
    kz3 = dt*D(x+.5*kx2, y+.5*ky2, z+.5*kz2, sig, rho, beta, 2)

    kx4 = dt*D(x+kx3, y+ky3, z+kz3, sig, rho, beta, 0)
    ky4 = dt*D(x+kx3, y+ky3, z+kz3, sig, rho, beta, 1)
    kz4 = dt*D(x+kx3, y+ky3, z+kz3, sig, rho, beta, 2)

    xn = x + (kx1 + 2*kx2 + 2*kx3 + kx4)/6
    yn = y + (ky1 + 2*ky2 + 2*ky3 + ky4)/6
    zn = z + (kz1 + 2*kz2 + 2*kz3 + kz4)/6
    return(xn, yn, zn)
def rossler(x, y, z, rho, sig, beta, ax, ax2):
    T, dt, t = 500, 0.01, 0
    xx, yy, zz, tt = [], [], [], []
    xx.append(x)
    yy.append(y)
    zz.append(z)
    tt.append(t)
    while(t<T):
        x, y, z = rk4(x, y, z, dt, sig, rho, beta)
        xx.append(x)
        yy.append(y)
        zz.append(z)    
        tt.append(t)
        t += dt
    lab = 'c= '+str(c)
    ax.plot(xx, yy, zz, label=lab)
    ax2.plot(tt, zz, '.', label=lab)
#########Plot Data#########
fig = plt.figure(1)
ax = fig.gca(projection='3d')
fig2 = plt.figure(2)
ax2 = fig2.gca()
c = 14
for i in range(4):
    rossler(2, 5,0, .1, .1, c, ax, ax2)
    c -= 4
ax.set_title(r'$R\"{o}ssler$ $Attractor$')
ax.legend()
ax2.legend()
ax2.set_ylabel('Z')
ax2.set_xlabel('time')
plt.show()    
