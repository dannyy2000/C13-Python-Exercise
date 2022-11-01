from class_exercise.first_class import FirstClass

if __name__ == '__main__':
    first = FirstClass("Daniel", 34)
    print("Initial record: ", first.__get_name__(), first.__get_age__())

    first.__set_name__("MicJohn")
    first.__set_age__(21)
    print("New record: ", first.__get_name__(), first.__get_age__())

