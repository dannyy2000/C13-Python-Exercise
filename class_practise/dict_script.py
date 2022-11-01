def convert(list_1, list_2):
    result = {list_1[a]: list_2[a] for a in range(len(list_1))}
    return result


if __name__ == '__main__':
    first_list = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninty', 'Hundred']
    second_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(convert(first_list, second_list))
