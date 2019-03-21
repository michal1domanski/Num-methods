from cs50 import get_string, get_float, get_int
from math import pi

def Count_field(name,x,y):
    if name == 'circle':
        return pi * x ** 2
    elif name == 'triangle' or name == 'rhombus':
        return x * y * 0.5
    else:
        return x * y

number_of_figures = get_int('How many figures would you like to compare?: ')
while number_of_figures <= 0:
    number_of_figures = get_int('How many figures would you like to compare?: ')

T = []
Fields = []

while number_of_figures > 0:
    number_of_figures -= 1
    name = get_string('Figure: ')
    name = name.lower()
    while True:
        if name == 'circle' or name == 'rectangle' or name == 'rhombus' or name == 'triangle':
            T.append(name)
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
    
    Fields.append(Count_field(name,x,y))
    
maximal_field = 0
z = []
tr = 0
for i in range(len(Fields)):
    if Fields[i] > maximal_field:
        maximal_field = Fields[i]
        tr = i
        z.clear()
        z.append(i+1)
    elif Fields[i] == maximal_field:
        z.append(i+1)

print(f"Maximal field belongs to {T[tr]} (figure numbers {z}) and it's equal = {Fields[tr]:.2f}")

    
