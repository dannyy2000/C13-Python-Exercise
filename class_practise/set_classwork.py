# if __name__ == '__main__':
#     user_input = (input("Enter 5 numbers: "))
#     if 2 <= user_input <= 90:
#         my_set = set(int(item) for item in user_input.split())
#         print(my_set)

if __name__ == '__main__':
    user_input = int(input('Enter space-separated integers: '))

    for i in range(6):

        if 2 <= user_input <= 90:
            # my_set = set(int(item) for item in user_input.split())
            my_set = set(user_input)
            print(my_set)

        else:
            print("Try again")

# my_set = set(input('Enter space-separated words: ').split())
