if __name__ == '__main__':
    tuition = 10_000
    total = 0

    for i in range(1, 11):
        tuition_inc = (tuition // 100) * 5
        tuition += tuition_inc
        print("$" + str(tuition))

    for i in range(1, 5):
        tuition_inc_4 = (tuition // 100) * 5
        tuition += tuition_inc_4 * 4
    total += tuition
    print("The total in 4 years is" + " " + "$" + str(total))
