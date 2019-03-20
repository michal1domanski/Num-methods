import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cs50 import get_float

value = get_float("value: ")

x_knots = np.linspace(-3*np.pi,3*np.pi,201)
y_knots = np.linspace(-3*np.pi,3*np.pi,201)
X, Y = np.meshgrid(x_knots,y_knots)
R = np.sqrt(X**2 + Y**2)*value
Z = np.cos(R)**(2+value)*np.exp(-0.1*R)
ax = Axes3D(plt.figure(figsize = (8,5)))
ax.plot_surface(X,Y,Z,rstride = 1,cstride = 1,cmap = plt.cm.inferno,linewidth = 3.5)
plt.show()