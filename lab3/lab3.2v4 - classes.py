from math import pi

class Figure:
    def __init__(self, figure, side1 = 0, side2 = 0, side3 = 0):
        self.figure = figure
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def c_field(self):
        if self.figure == 'circle':
            field = pi * self.side1 ** 2
        elif self.figure == 'rectangle':
            field = self.side1 * self.side2
        elif self.figure == 'rhombus' or self.figure == 'triangle':
            field = self.side1 * self.side2 * 0.5
        elif self.figure == 'trapeze':
            field = ((self.side1 + self.side2) * self.side3) * 0.5
        return field

def compare_fields(field1, field2):
    if field1 > field2:
        return print('field 1 [', field1, '] is bigger [', figure1.figure, ']')
    elif field1 < field2:
        return print('field 2 [', field2, '] is bigger [',figure2.figure,']')
    else:
        return print('fields are equal ',field1,' ',field2)

figure1 = Figure('rhombus', 12,18)
figure2 = Figure('trapeze', 10,12,10)
if figure1.side1 < 0 or figure1.side2 < 0 or figure1.side3 < 0:
    print('Your mom gay')
    field1 = 0
else:
    field1 = figure1.c_field()

if figure2.side1 < 0 or figure2.side2 < 0 or figure2.side3 < 0:
    print('Your mom gay')
    field2 = 0
else:
    field2 = figure2.c_field()

compare_fields(field1,field2)
    