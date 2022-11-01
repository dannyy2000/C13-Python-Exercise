if __name__ == '__main__':
    weight = int(input("Enter your weight: "))
    unit = (input('(L)bs or (K)g: '))

    if unit.upper() == 'L':
        conversion = weight * 0.45359237
        print(f'You are {conversion} kilos')
    elif unit.upper() == 'K':
        conversion = weight * 2.2046
        print(f'You are {conversion} pounds')
    else:
        print('Enter a valid unit')

