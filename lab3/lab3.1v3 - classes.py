from cs50 import get_float, get_string
from math import pi

class Figure():
    def __init__ (self,name,side1):
        self.name = name
        self.side1 = side1

    def field(self):
        if self.name == 'triangle':
            field = self.side1[0] * self.side1[1] / 2
        elif self.name == 'rhombus':
            field = self.side1[0] * self.side1[1] / 2
        elif self.name == 'circle':
            field = (self.side1[0]**2) * pi 
        elif self.name == 'rectangle':
            field = self.side1[0] * self.side1[1]
        elif self.name == 'trapeze':
            field = ((self.side1[0] + self.side1[1]) * self.side1[2]) / 2
        return field
    
    def perimeter(self):
        if self.name == 'circle':
            perimeter = self.side1[0] * 2 * pi
            perimeter = round(perimeter,2)
        elif self.name == 'rectangle':
            perimeter = self.side1[0] * 2 + self.side1[1] * 2
            perimeter = round(perimeter,2)
        else:
            perimeter = 'Imposible, perhaps the archives are incomplete...'
        return perimeter

a = Figure('trapeze',[12,13,2])
print(round(a.field(),2))
print(a.perimeter())

# while i < 2:
#     figure = get_string('What figure would you like to measure?: ')
#     figure = figure.lower()
#     if figure == 'circle':
#         c.side1.append(get_float('Perimeter: '))
#         c.field = pi*c.side1[0]**2
#         print(c.name,round(c.field,2),c.side1)
#         i+=1
#     elif figure == 'rhombus':
#         b.side1.append(get_float('Diagonal one: '))
#         b.side1.append(get_float('Diagonal two: '))
#         b.field = b.side1[0]*b.side1[1]/2
#         print(b.name,round(b.field,2),b.side1)
#         i+=1
#     elif figure == 'triangle':
#         a.side1.append(get_float('Base: '))
#         a.side1.append(get_float('Height: '))
#         a.field = a.side1[0]*a.side1[1]/2
#         print(a.name,round(a.field,2),a.side1)
#         i+=1
#     elif figure == 'rectangle':
#         d.side1.append(get_float('Side one: '))
#         d.side1.append(get_float('Side two: '))
#         d.field = d.side1[0]*b.side1[1]
#         print(d.name,round(d.field,2),d.side1)
#         i+=1
#     else:
#         e.side1.append(get_float('base one: '))
#         e.side1.append(get_float('base two: '))
#         e.side1.append(get_float('height: '))
#         e.field = ((e.side1[0]+e.side1[1])*e.side1[2])/2
#         print(e.name,round(e.field,2),e.side1)
#         i+=1


