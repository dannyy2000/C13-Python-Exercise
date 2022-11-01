import random


def modify_guess():
    random_number = random.randint(1, 1000)
    counter = 0
    print(random_number)
    guessed_number = int(input("Enter your number: "))
    counter += 1

    while guessed_number != random_number:
        if guessed_number > random_number:
            print("too high")
        else:
            print("too low")
        guessed_number = int(input("Enter your number"))
        counter += 1
    else:
        print("Congratulations, You guessed the number!! ")
        if counter <= 10:
            print('Aha! You know the secret')
        else:
            print("You should be able to do better!\n why should it take more than 10 guesses? ")
            answer = input("Do you want to play again:")
            if answer.lower() == 'yes':
                modify_guess()


if __name__ == '__main__':
    modify_guess()
