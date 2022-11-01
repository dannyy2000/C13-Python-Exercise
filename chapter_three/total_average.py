if __name__ == '__main__':
    total = 0
    counter = 0

    grade = int(input("Enter grade or -1 to stop: "))

    while grade != -1:
     grade = int(input("Enter grade or -1 to stop: "))
     total = total + grade
     counter = counter + 1

    if counter != 0:
        average = float(total) / counter
        print("The average is", average)
    else:
        print("No grades entered")


