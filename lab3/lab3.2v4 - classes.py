from math import pi

class Figure:
    def __init__(self, figure, *sides):
        self.figure = figure
        self.sides = sides

    def c_field(self):
        # dodaj tutaj fori i in range(2) zeby dwa razy zwrociło ci wartosć i dodaj compare fields do klasy
        if self.figure.lower() == 'circle':
            field = pi * self.sides[0] ** 2
        elif self.figure.lower() == 'rectangle':
            field = self.sides[0] * self.sides[1]
        elif self.figure.lower() == 'rhombus' or self.figure == 'triangle':
            field = self.sides[0] * self.sides[1] / 2
        elif self.figure.lower() == 'trapeze':
            field = ((self.sides[0] + self.sides[1]) * self.sides[2]) / 2
        return round(field,2)

def compare_fields(field1, field2):
    if field1 > field2:
        return print('field 1 [', field1, '] is bigger \n[', figure1.figure.upper(), ']')
    elif field1 < field2:
        return print('field 2 [', field2, '] is bigger \n[',figure2.figure.upper(),']')
    else:
        return print('fields are equal ',field1,' ',field2)

figure1 = Figure('CiRcLe', 13, 17, 12)
figure2 = Figure('triangle', 13, 17)
field1 = Figure.c_field(figure1)
field2 = Figure.c_field(figure2)
compare_fields(field1,field2)
