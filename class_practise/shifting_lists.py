if __name__ == '__main__':

    months = ["january", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December" ]
    monthNumber = eval(input("Enter a month number (1 to 12): "))
    print("The month is", months[monthNumber - 1])
    # def shift(lst):
    #     lst = [2, 5, 7, 8, 9]
    #     temp = lst[1]
    #
    #     for i in range(1, len(lst)):
    #         lst[i - 1] = lst[i]
    #
    #     lst[len(lst) - 1] = temp
    #     print(lst)

# if __name__ == '__main__':
# shift([2, 3, 1, 4, 6, 3, 7])
# # print(shift([2, 3, 1, 4, 6, 3, 7]))
# print(shift(lst=[2, 3, 1, 4, 6, 3, 7]))
