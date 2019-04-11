from math import pi

class Figure:
    def __init__(self, figure, *sides):
        self.figure = figure
        self.sides = sides

    def c_field(self):
        # dodaj tutaj fori i in range(2) zeby dwa razy zwrociło ci wartosć i dodaj compare fields do klasy
        if self.figure == 'circle':
            field = pi * self.sides[0] ** 2
        elif self.figure == 'rectangle':
            field = self.sides[0] * self.sides[1]
        elif self.figure == 'rhombus' or self.figure == 'triangle':
            field = self.sides[0] * self.sides[1] / 2
        elif self.figure == 'trapeze':
            field = ((self.sides[0] + self.sides[1]) * self.sides[2]) / 2
        return round(field,2)

def compare_fields(field1, field2):
    if field1 > field2:
        return print('field 1 [', field1, '] is bigger [', figure1.figure, ']')
    elif field1 < field2:
        return print('field 2 [', field2, '] is bigger [',figure2.figure,']')
    else:
        return print('fields are equal ',field1,' ',field2)

figure1 = Figure('trapeze', 13, 17)
figure2 = Figure('triangle', 13, 17)
field1 = Figure.c_field(figure1)
field2 = Figure.c_field(figure2)
compare_fields(field1,field2)
    