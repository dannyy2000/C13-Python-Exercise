def calculate_charges(no_of_hours):
    pass


def display_charges():
    print(f'The total charges is %.2f' % calculate_charges(no_of_hours=3))


# def calculate_charges(no_of_hours):
#     charges = 0
#     minimum_charge = 2.00
#     if no_of_hours <= 3:
#         charges += minimum_charge
#
#     elif no_of_hours > 3:
#         additional_charges = (no_of_hours - 3) * 0.5
#         charges = additional_charges + minimum_charge
#
#     return charges


# def calculate_charges(no_of_hours):
#     pass


class ParkingCharges:
    def __set_name__(self, name):
        self.name = name

    def _get_name__(self):
        return self.name

    def calculate_charges(self, no_of_hours):
        charges = 0
        minimum_charge = 2.00
        if no_of_hours <= 3:
            charges += minimum_charge

        elif no_of_hours > 3:
            additional_charges = (no_of_hours - 3) * 0.5
            charges = additional_charges + minimum_charge

        return charges

    # def display_charges():
    #     print(f'The total charges is %.2f' % calculate_charges(no_of_hours=3))
    #