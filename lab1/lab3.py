from numpy import *
from matplotlib.pyplot import *

#zadanie 3
def z3():
    print("How big should the array be?")
    a = float(input())
    while a <= 0 or a % 1 != 0:
        print("Not this time Mr Bond. Try again")
        a = float(input())
    i = 0
    T=[]
    while i < a:
        print("Add a number to an array")
        T.append(float(input()))
        i += 1
    mi = []
    mv = min(T)
    for x in range(len(T)):
        if T[x] == mv:
            mi.append(x)
    print(f"Your array: {T}")
    print(f"Lowest value is: {mv}, and it's index is: {mi}")
z3()