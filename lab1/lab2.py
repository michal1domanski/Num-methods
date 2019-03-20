from numpy import *
from matplotlib.pyplot import *

#zadanie 2
print("Insert value here: ")
a = float(input())
if a < 0 or a % 1 != 0:
    print("This number is incorrect")
    while a < 0 or a % 1 != 0:
        print("Try Again: ")
        a = float(input())
i = 1
b = 1
while i<=a:
    b = b * i
    i += 1
print(b)