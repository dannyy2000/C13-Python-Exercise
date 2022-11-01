import math

if __name__ == '__main__':
    value_a = int(input("Enter the value for a"))
    value_b = int(input("Enter the value of b"))
    value_c = int(input("Enter the value of c"))

    r1 = (-value_b) + math.sqrt(value_b * value_b - 4 * value_a * value_c) // 2 * value_a
    r2 = (-value_b) - math.sqrt(value_b * value_b - 4 * value_a * value_c) // 2 * value_a

    if r1 and r2 == 0:
        print("it has no roots")
