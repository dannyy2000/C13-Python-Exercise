if __name__ == '__main__':
    import random
    import time

    countResult = 0
    count = 0

    No_Of_Question = 5
    start_time = time.time()

    while count < No_Of_Question:
        number1 = random.randint(1, 15)
        number2 = random.randint(1, 15)

        answer = eval(input("What is" + " " + str(number1) + " + " + str(number2) + "?" + ":"))

        if number1 + number2 == answer:
            print("Good job, you are correct")
            countResult += 1

        else:
            print("Incorrect answer")

        count += 1

    end_time = time.time()
    test_time = int(end_time - start_time)

    print("The students got", countResult, "out of", No_Of_Question, "in", test_time , "seconds")
