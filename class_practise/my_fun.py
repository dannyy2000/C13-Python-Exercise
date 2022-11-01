def my_fun(param):
    param = [1, 2, 3]
    param.append(4)
    return param


list_i = [1, 2, 3, 4, 5, 6, 7]
value = my_fun(list_i)
print(value)
