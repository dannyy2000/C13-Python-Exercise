from class_practise.parking_charges import ParkingCharges
if __name__ == '__main__':
    my_parking_charges = ParkingCharges

    for i in range(3):
        #my_parking_charges.__set_name__(self= name=)(print("Enter your name: "))
        print(my_parking_charges.calculate_charges(no_of_hours=3))
        my_parking_charges.display_charges()
