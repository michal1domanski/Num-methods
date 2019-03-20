from numpy import *

print("X circle radius")
radiusx = float(input())
while radiusx < 0:
    print("X circle radius")
    radiusx = float(input())

print("Y circle radius")
radiusy = float(input())
while radiusy < 0:
    print("Y circle radius")
    radiusy = float(input())

print(f"Field of circle X is {pi*(radiusx)**2:.2f}, field of circle X is {2*pi*radiusx:.2f}")
print(f"Field of circle Y is {pi*(radiusy)**2:.2f}, field of circle Y is {2*pi*radiusy:.2f}")

print(f"Field of X and Y ring is {abs(pi*(radiusx)**2 - pi*(radiusy)**2):.2f}")
print(f"Perimeter of X and Y ring is {2*pi*radiusx + 2*pi*radiusy:.2f}")