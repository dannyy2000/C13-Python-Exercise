def odd(myList):
    for i in range(0, len(numbers), 2):
        print(numbers[i])
        #return numbers[i]


if __name__ == '__main__':
    numbers = [1, 3, 4, 7, 2, 6, 9, 8]
    print(odd(numbers))
