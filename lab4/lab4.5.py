from scipy import linspace , cos , exp, random, meshgrid, zeros, sin, sqrt
from scipy.optimize import fmin
from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel
from scipy.optimize import differential_evolution
from mpl_toolkits.mplot3d import Axes3D

def f(x):
    return sin(sqrt((x[0]**2)+(x[1]**2)))/sqrt((x[0]**2)+(x[1]**2))


x0 = [0,-8]
x_min = fmin(f, x0)

delta = -15
x_knots = linspace(x_min[0] - delta, x_min[0] + delta, 41)
y_knots = linspace(x_min[1] - delta, x_min[1] + delta, 41)
X, Y = meshgrid(x_knots, y_knots)
Z = zeros(X.shape)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])

ax = Axes3D(figure(figsize=(8, 5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.4)
ax.plot([x0[0]], [x0[1]], [f(x0)], color='g', marker='o', markersize=5, label='initial')
ax.plot([x_min[0]], [x_min[1]], [f(x_min)], color='k', marker='o', markersize=5, label='final')
ax.legend()
bounds = [(-5, 5), (-5, 5)]
result = differential_evolution(f, bounds)
print(result.x, result.fun)
ax.plot([result.x[0]],[result.x[1]], [result.fun],marker = 'o', markersize = 5, color = '101010')
show()
