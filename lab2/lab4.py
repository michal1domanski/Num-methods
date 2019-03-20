from cs50 import get_float

X = get_float('X: ')
Y = get_float('Y: ')
while Y == 0:
    print("NOPE")
    Y = get_float('Y: ')
print('X is divisable by Y' if X % Y == 0 else 'X is NOT divisable by Y')
print(f"X/Y is: {X/Y:.2f}")