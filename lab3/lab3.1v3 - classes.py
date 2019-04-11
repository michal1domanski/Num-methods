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
    
    # def perimeter(self):
    #     if self.name == 'circle':
    #         perimeter = self.side1[0] * 2 * pi
    #         perimeter = round(perimeter,2)
    #     elif self.name == 'rectangle':
    #         perimeter = self.side1[0] * 2 + self.side1[1] * 2
    #         perimeter = round(perimeter,2)
    #     else:
    #         perimeter = 'Imposible, perhaps the archives are incomplete...'
    #     return perimeter

a = Figure('trapeze',[12,13,12])

print(round(a.field(),2))
# print(a.perimeter())



