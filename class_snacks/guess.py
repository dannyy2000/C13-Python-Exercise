import random


def guess():
    random_number = random.randint(1, 1000)
    print(random_number)
    guess_number = int(input("Enter a number: "))
    while guess_number != random_number:
        if guess_number > random_number:
            print("Too high")
        else:
            print("Too low")
        guess_number = int(input("Enter a number: "))
    else:
        print("Congratulations,you guessed right")
        answer = input("Do you want to play again? ")
        if answer.lower() == 'yes':
            guess()


if __name__ == '__main__':
    guess()
