import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

m=50
g=9.81
rho=1.091
A=np.pi*0.5**2
ve=325
Cd=0.15
mp=100

def burnrate(t):
    if t<5: return 20
    return 0

#h, v, m
def diff(x, t):
    return [x[1], -g+burnrate(t)*ve/(m+x[2])-0.5*rho*x[1]*np.abs(x[1])*A*Cd/(m+x[2]), -burnrate(t)]

T=np.linspace(0,40,200000)
X0=[0,0,mp]
Y=odeint(diff, X0, T)

for n in range(3):
    plt.figure(n+1)
    plt.plot(T,Y[:,n])

plt.show()

