if __name__ == '__main__':
    number1 = int(input("Enter the first integer: "))
    number2 = int(input("Enter the second integer: "))
    number3 = int(input("Enter the third integer: "))

    largest = number1
    if number2 > number1:
        number2 = largest

    if number3 > number1:
        number3 = largest

    largest = number2
    if number1 > number2:
        number1 = largest

    if number3 > number2:
        number3 = largest

    largest = number3
    if number1 > number3:
        number1 = largest

    if number2 > number3:
        number2 = largest

print(f"The number in increasing form is ")