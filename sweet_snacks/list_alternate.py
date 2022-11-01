def alternate(list1, list2):
    return [sub[item] for item in range(len(list2))
            for sub in [list1, list2]]


if __name__ == '__main__':
    first_list = ['a', 'b', 'c']
    second_list = [1, 2, 3]
    print(alternate(first_list, second_list))
