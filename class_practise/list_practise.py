if __name__ == '__main__':
    number_of_elements = 5
    numbers = []
    total = 0

    for i in range(number_of_elements):
        value = eval(input("Enter a new number"))
        numbers.append(value)
        total += value

    average = total / number_of_elements

    count = 0
    for i in range(number_of_elements):
        if numbers[i] > average:
            count += 1

    print("The average is ", average)
    print("The number of count above average is", count)