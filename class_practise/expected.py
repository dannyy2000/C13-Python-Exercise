import math


def dominos(pizza_amount, current_balance, offender_fee):
    return math.ceil((pizza_amount - current_balance) / offender_fee)



if __name__ == '__main__':
    print("The total no of people if they are paying 100:", dominos(10000, 4300, 100))
    print("The total no of people if they are paying 200:", dominos(10000, 4300, 200))
    print("The total no of people if they are paying 500:", dominos(10000, 4300, 500))
    print("The total no of people if they are paying 1000:", dominos(10000, 4300, 1000))




