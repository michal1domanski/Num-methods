from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def F(x,t):
    dx = [0,0]
    dx[0] = x[1] * 3
    dx[1] = - x[0] - 0.5 * -0.76517626 * x[1]
    return dx

t_min = -3
t_max = 17
h = 0.001
t = np.arange(t_min, t_max+h, h)

initial_x = ((1,0))

X = odeint(F, initial_x, t)
plt.figure(1)
plt.plot(t,X)
plt.figure(2)
plt.plot(X[:,0],X[:,1])
plt.axis('equal')
plt.show()
