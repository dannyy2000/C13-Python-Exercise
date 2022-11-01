import operator


def calculator():
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    if operator == '*':
        print(f'The first number multiplied by the second number is {first_number} * {second_number}=', abs(first_number
                * second_number))
    if operator == '+':
        print(f'The first number added to the second number is {first_number} + {second_number} =', abs(first_number +
                                                                                                        second_number))
    if operator == '-':
        print(f'The first number  by the second number{first_number} - {second_number} = ', abs(first_number -
              second_number))

    if __name__ == '__main__':

        calculator()
