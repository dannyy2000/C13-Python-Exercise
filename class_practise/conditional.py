if __name__ == '__main__':
    n = int(input("Enter an integer: "))

    value1 = 2 <= n <= 5
    value2 = 6 <= n <= 20
    value3 = n > 20

    if n % 2 != 0:
        print("Weird")
    if n % 2 == 0 and value1:
        print("Not weird")
    if n % 2 == 0 and value2:
        print("Weird")
    if n % 2 == 0 and value3:
        print("Not weird")
  