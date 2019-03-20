from cs50 import get_string,get_float

def comparingFields():
    name1.lower() = get_string('first figure: ')
    while name1 != 'circle' or name1 != 'rectangle' or name1 != 'triangle' or name1 != 'rhombus':
        name1.lower() = get_string('Try again: ')

    if name1 == 'circle':
        radius = get_float('radius: ')
        while radius <=0:
            print('Try again')
            radius = get_float('radius: ')
    elif name1 == 'rectangle':
        side1 = get_float('First side: ')
        while side1 <=0:
            print('Try again')
            side1 = get_float('First side: ')
        side2 = get_float('Second side: ')
        while side2 <=0:
            print('Try again')
            side2 = get_float('Second side: ')
    elif name1 == 'triangle':
        base = get_float('Base: ')
        while base <=0:
            print('Try again')
            base = get_float('Base: ')
        height = get_float('Height: ')
        while height <=0:
            print('Try again')
            height = get_float('height: ')
    elif name1 == 'rhombus':
        diagonal1 = get_float('First diagonal: ')
        while diagonal1 <= 0:
            print('Try again')
            diagonal1 = get_float('First diagonal:')
        diagonal2 = get_float('Second diagonal: ')
        while diagonal2 <= 0:
            print('Try again')
            diagonal2 = get_float('Second diagonal:')
    print(name1)


    name2.lower() = get_string('second figure: ')
    while name2 != 'circle' or name2 != 'rectangle' or name2 != 'triangle' or name2 != 'rhombus':
        name2.lower() = get_string('Try again: ')

print(comparingFields())