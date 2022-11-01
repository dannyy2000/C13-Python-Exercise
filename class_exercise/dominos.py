import math


def dodo_pizza(pizza_amount, current_balance, offender):
   pizza_amount = print(int(input("Enter the amount of pizza: ")))
   print(int(input("Enter the current balance: ")))
   print(int(input("Enter the no of offender: ")))
   return math.ceil(pizza_amount - current_balance / offender)

if __name__ == '__main__':
   print(dodo_pizza("The total no of people if they are paying"))






