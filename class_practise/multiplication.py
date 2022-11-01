def multiplication():
    number = int(input("Enter a number: "))
    for multiply in range(1, 13):
        print(f'{number} * {multiply} =', number * multiply)


if __name__ == '__main__':
    multiplication()
