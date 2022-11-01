if __name__ == '__main__':

    number = int(input("Enter a number: "))
    total = 0
    print("The factors are: ", end=' ')

    for i in range(1, number):
        if number % i == 0:
            print(i, end=' ')
            total+=i

    print("\nsum of the factor is: ", total)

    if number == total:
        print("The number is perfect")
    else:
        print("The number is not perfect")
