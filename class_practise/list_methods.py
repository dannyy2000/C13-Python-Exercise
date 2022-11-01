if __name__ == '__main__':
    # list1 = [2, 5, 8, 3, 0, 2]
    # list2 = [3, 5, 1, 9]
    # list1.extend(list2)
    # print(list1)
    # list1.append(20)
    # print(list1)
    #
    # list1.count(0)
    # print(list1.extend(list1))
    #
    # print(list1.count(0))
    # print(list1.insert(8,5))
    # print(list1)
    # print(list1.sort())
    # print(list1)

    # print(list1.pop(0))
    # print(list1)
    # print(list1.pop())
    # print(list1)

    s = input("Enter 10 numbers seperated by spaces from one line")
    items = s.split()
    # list_1 = [eval(s) for s in items]
    # print(list_1)
    print(items)

    s = input("Enter 10 numbers seperated by spaces from one line")
    items = s.split()
    list_1 = [eval(s) for s in items]
    print(list_1)
    print(items)

    # lst = []
    # print("Enter 10 numbers: ")
    # for i in range(10):
    #     lst.append(eval(input()))
    # print(lst)