def celsius_of(kelvin):
    return kelvin - 273.15


if __name__ == '__main__':
    temp = int(input("Enter a celsius temperature: "))
    print(f'{temp} in celsius is {celsius_of(30)}')
