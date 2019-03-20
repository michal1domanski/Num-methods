from cs50 import get_float,get_string,get_int
from math import pi

def countField():
    print('You can type in: 1 - triangle, 2 - circle, 3 - rectangle, 4 - rhombus')
    number = get_int('What number figure field you want to count? ')
    while number > 4 or number < 1:
        print('Wrong number')
        print('1 - triangle, 2 - circle, 3 - rectangle, 4 - rhombus')
        number = get_int('Try again: ')

    if number == 1:
        x = get_float('base: ')
        while x <= 0:
            print('lenght cannot be a negative number')
            x = get_float('base: ')
    
        y = get_float('height: ')
        while y <= 0:
            print('lenght cannot be a negative number')
            y = get_float('height: ')

        field = x * y * 0.5

    elif number == 2:
        x = get_float('radius: ')
        while x <= 0:
            print('lenght cannot be a negative number')
            x = get_float('radius: ')
            
        field = pi * (x ** 2)

    elif number == 3:
        x = get_float('side one: ')
        while x <= 0:
            print('lenght cannot be a negative number')
            x = get_float('side one: ')
    
        y = get_float('side two: ')
        while y <= 0:
            print('lenght cannot be a negative number')
            y = get_float('side two: ')
            
        field = x * y

    elif number == 4:
        x = get_float('first diagonal: ')
        while x <= 0:
            print('lenght cannot be a negative number')
            x = get_float('first diagonal: ')
    
        y = get_float('second diagonal: ')
        while y <= 0:
            print('lenght cannot be a negative number')
            y = get_float('second diagonal: ')
            
        field = x * y * 0.5

    return field

print(f'field = {countField():.2f}')