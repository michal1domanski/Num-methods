from cs50 import get_string, get_float
from math import pi

def Count_field(name,x,y = None):
    if name == 'circle':
        return pi * x ** 2
    elif name == 'triangle' or name == 'rhombus':
        return x * y * 0.5
    else:
        return x * y

name = get_string('Figure: ')
name = name.lower()

while True:
    if name == 'circle' or name == 'rectangle' or name == 'rhombus' or name == 'triangle':
        break
    else:
        name = get_string('Figure: ')
        name = name.lower()

x = get_float('First lenght: ')
while x <= 0:
    x = get_float('First lenght: ')
y = 0
if name != 'circle':
    y = get_float('Second lenght: ')
    while y <= 0:
        y = get_float('Second lenght: ')

print(f'Field = {Count_field(name,x,y):.2f}')