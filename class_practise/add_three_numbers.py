import random

if __name__ == '__main__':
    number1 = random.randint(0, 10)
    number2 = random.randint(0, 10)
    number3 = random.randint(0, 10)

    answer = eval(input("what is " + str(number1) + "+" + str(number2) + "+" + str(number3) + " ? " ))

    print(number1, "+", number2, "+", number3, "=", number1 + number2 + number3 == answer)
