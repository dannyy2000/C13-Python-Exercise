def contain(myList):
    num = ([2, 4, 5, 6, 7, 8])

    if number in num:
        return "True"
    else:
        return "False"


if __name__ == '__main__':
    number = int(input("Enter the an elements in the list: "))
    print(contain(number))
