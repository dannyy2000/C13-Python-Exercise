if __name__ == '__main__':
    counter = 0
    secret_number = 5

    while counter != secret_number:
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print("Correct!!!")
            break
        else:
            print("try again!!!")

        counter += 1