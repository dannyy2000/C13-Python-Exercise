if __name__ == '__main__':
    word = input("Enter the value: ")

    reverse = word[::-1]

    if word == reverse:
        print("It is a palindrome")
    else:
        print("It is not a palindrome ")