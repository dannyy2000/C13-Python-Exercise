def sorted_list(word1, word2):
    return sorted(word1) + sorted(str(word2))


if __name__ == '__main__':
    first_word = input("Enter a word: ")
    sec_word = int(input("enter some integers"))
    print(sorted_list(first_word, sec_word))
