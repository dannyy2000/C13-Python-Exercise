if __name__ == '__main__':
    counter = 1
    passed = 0
    failed = 0

    while counter <= 10:
        grade = int(input("Enter result,1 if passed or 2 if failed:"))
        counter = counter + 1

        if grade == 1:
         passed = passed + 1

        else:
         failed = failed + 1

        counter = counter + 1

    print("passes",passed)
    print("failures",failed)

    if passed > 8:
        print("Raise tuition")

