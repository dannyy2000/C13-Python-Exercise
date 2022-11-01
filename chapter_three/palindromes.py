def palindrome():
    word = input("Enter a statement: ")
    reverse = word[::-1]
    print (reverse)
    if reverse == word:
        print("The statement is a palindrome")
    else:
        print("The statement is not a palindrome")

if __name__ =='__main__':
    palindrome()