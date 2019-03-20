from cs50 import get_float, get_string
from math import pi

def trianglerhombus():
    x = get_float('first: ')
    while x <= 0:
        x = get_float('first: ')
    y = get_float('second: ')
    while y <= 0:
        y = get_float('second: ')
    return x*y*0.5

def circle():
    radius = get_float('radius: ')
    while radius <=0:
        radius = get_float('radius: ')
    return pi*radius**2

def rectangle():
    a = get_float('side one: ')
    while a <= 0:
        a = get_float('side one: ')
    b = get_float('side two: ')
    while b <= 0:
        b = get_float('side two: ')
    return a*b

def comparingfields():
    name1 = get_string('first figure name: ')
    lname1 = name1.lower()
    print(lname1)
    while lname1 != "circle" and lname1 != "triangle" and lname1 != "rectangle" and lname1 != "rhombus":
        name1 = get_string('first figure name: ')
        lname1 = name1.lower()
        print(lname1)
    if lname1 == 'triangle' or lname1 == 'rhombus':
        field1 = trianglerhombus()
    elif lname1 == 'circle':
        field1 = circle()
    elif lname1 == 'rectangle':
        field1 = rectangle()
    
    name2 = get_string('second figure name: ')
    lname2 = name2.lower()
    while lname2 != 'circle' and lname2 != 'triangle' and lname2 != 'rectangle' and lname2 != 'rhombus':
        name2 = get_string('second figure name: ')
        lname2 = name2.lower()
    if lname2 == 'triangle' or lname2 == 'rhombus':
        field2 = trianglerhombus()
    elif lname2 == 'circle':
        field2 = circle()
    elif lname2 == 'rectangle':
        field2 = rectangle()
    
    if field1 < field2:
        print(f'The second Figure [{lname2}] has larger field')
    elif field1 > field2:
        print(f'The first Figure [{lname1}] has larger field')
    else:
        print(f'The fields of [{lname1}] and [{lname2}] are equal')

comparingfields()