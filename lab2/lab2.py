from cs50 import get_float

X = get_float('X: ')

Y = get_float('Y: ')
while Y == 0:
    print("You cannot divde by 0")
    Y = get_float('Y: ')
if X % Y == 0 and X % 2 == 0 and Y % 2 == 0:
    print("X is divisable by Y and both are even")
    print(X%Y+0)
else:
    print("The statement is incorrect") 