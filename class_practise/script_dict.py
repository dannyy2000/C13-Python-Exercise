def script_generate(number):
    items = dict()
    for x in range(1, number+1):
        items[x] = x * x
    return items


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    print(script_generate(num))