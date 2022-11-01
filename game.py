import random

if __name__ == '__main__':
   # random.seed(104)

    number = random.randint(1, 10)

    counter = 1

    while counter <= 3:

     guess = int(input("Guess a number between 1 and 10:"))

     if guess > number:
        print("Too high")
     elif guess == number:
         print("Correct")
         break
     else:
         print("Too low")

     counter+=1



