import math


def hypotenuse_of(side_1, side_2):
    squares = math.pow(side_1, 2) + math.pow(side_2, 2)
    return math.sqrt(squares)


if __name__ == '__main__':
    side = int(input("Enter the length of side1"))
    sides = int(input("Enter the length of side2"))
    print(f'The hypotenuse is {hypotenuse_of(side_1=2,side_2=6)}')
