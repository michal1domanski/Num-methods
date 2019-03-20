from numpy import *
from matplotlib.pyplot import *

#zadanie 4
print("First side of chart")
a = float(input())
print("Second side of chart")
b = float(input())
if b == a:
    print("the chart would be empty, don't do it")
    while b == a:
        print("Second side of chart")
        b = float(input())
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16}
x = linspace(a,b,300)
y = sin(19.85*x)*sin(x)
plot(x,y,'k-',label="Legends are cool")
title("AM",fontdict = font)
xlabel('X line',fontdict = font)
ylabel('Y line',fontdict = font)
axhline(color = 'gray', zorder=0)
axvline(color = 'gray', zorder=0)
legend(loc = "upper right")
ylim(-1.5,1.5)
xlim(a,b)
subplots_adjust(left=0.15)
show()