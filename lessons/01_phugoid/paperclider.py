import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import random
from scipy.integrate import odeint

g=9.81
ld=5.0
vt=4.9

y0=2.0
x0=0.0
t0=0.0
T=np.linspace(0,10,200)

#v, rho, x, y
def f(x, t):
    return [-g*np.sin(x[1])-1/ld*g*x[0]**2/vt**2,
            -g/x[0]*np.cos(x[1])+g/vt**2*x[0],
            x[0]*np.cos(x[1]),
            x[0]*np.sin(x[1])]

Rho, V, X=[],[],[]
for n in range(300):
    v0=random.random()*60
    rho0=(random.random()-0.5)*np.pi/2

    Y=odeint(f, [v0, rho0, x0, y0], T)
    
    x=next(y[2] for y in Y if y[3]<0)
    print(next(y[1] for y in zip(Y,T) if y[0][3]<0))
    X.append(x)
    V.append(v0)
    Rho.append(rho0)


fig=plt.figure()
ax=fig.gca(projection='3d')
ax.plot_trisurf(V, Rho, X, cmap=cm.jet, linewidth=0.2)
plt.show()

