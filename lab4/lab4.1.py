from cs50 import get_float
from numpy import *
from matplotlib.pyplot import *

def Euler():
    a = 1
    T = 3
    h = 0.1
    
    initial_x = 1
    t = arange(0, T, h)
    x = zeros(t.shape)
    x[0] = initial_x

    for i in range(t.size-1):
        x[i+1] = x[i] + h * (1 * x[i])

    h = 0.001
    initial_y = 1
    r = arange(0,T,h)
    y = zeros(r.shape)
    y[0] = initial_y
    for i in range(r.size-1):
        y[i+1] = y[i] + h * (1 * y[i])
    plot(t,x,'-')
    plot(r,y,'g-')
    show()

Euler()



