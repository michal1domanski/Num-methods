from numpy import *
from cs50 import get_float

radiusx = get_float('X circle radius: ')
while radiusx <= 0:
    print("Wrong try again")
    radiusx = get_float('X circle radius: ')

radiusy = get_float('Y circle radius: ')
while radiusy <= 0:
    print("Wrong try again")
    radiusy = get_float('Y circle radius: ')

print(f"Field of circle X is {pi*(radiusx)**2:.2f}, perimeter of circle X is {2*pi*radiusx:.2f}")
print(f"Field of circle Y is {pi*(radiusy)**2:.2f}, permieter of circle Y is {2*pi*radiusy:.2f}")

print(f"Field of X and Y ring is {abs(pi*(radiusx)**2 - pi*(radiusy)**2):.2f}")
print(f"Perimeter of X and Y ring is {2*pi*radiusx + 2*pi*radiusy:.2f}")