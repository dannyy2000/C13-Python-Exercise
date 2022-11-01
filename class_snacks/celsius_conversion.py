def kelvin_of(celsius):
    return celsius + 273.15


if __name__ == '__main__':
    temp = int(input("Enter a celsius temperature: "))
    print(f'{temp} in celsius is {kelvin_of(20)}')
