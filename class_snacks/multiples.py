def is_multiple(num_1, num_2):
    if not num_2 % num_1:

        return True

    else:

        return False


if __name__ == '__main__':
    for count in range(3):

        first_num = int(input('Enter the first number: '))

        second_num = int(input('Enter the second number: '))

        if is_multiple(first_num, second_num):

            print(f'{second_num} is a multiple of {first_num}')

        else:

            print(f'{second_num} is not a multiple of {first_num}')
