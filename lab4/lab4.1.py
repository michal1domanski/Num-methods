from cs50 import get_float
from numpy import *
from matplotlib.pyplot import *

def Euler():
    a = get_float('a: ')
    T = get_float('T: ')
    while T <= 0:
        T = get_float('T; ')
    h = get_float('h: ')
    while h <= 0:
        h = get_float('h: ')
    initial_x = get_float('x: ')

    t = arange(0, T, h)
    x = zeros(t.shape)
    x[0] = initial_x

    for i in range(t.size-1):
        x[i+1] = x[i] + h * (1 * x[i])
    
    plot(t,x,'o')
    show()

Euler()