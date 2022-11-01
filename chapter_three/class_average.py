if __name__ == '__main__':
    counter = 0
    total = 0

    while counter <= 10:
        grade = int(input("Enter grade: "))
        total = total + grade
        counter = counter + 1

    average = total / 10
    print("The average is",average)

