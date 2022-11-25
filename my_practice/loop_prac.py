if __name__ == '__main__':
    average = 0
    counterPos = 0
    counterNeg = 0
    total = 0
    counter = 0

    number = int(input("Enter a number: "))
    while number != counter:
        number = int(input("Enter a number: "))
        if number < 0:
            counterNeg += 1

        elif number > 0:
            counterPos += 1

        else:
            print("You didnt enter a number")
        total += 1
    counter += 1

    if number == 0:
        average = counterPos / counter or counterNeg / counter

        print("The total number is", total)
        print("The average number is", average)
        print("The number of positives is: ", counterPos)
        print("The number of negatives is: ", counterNeg)
