def convert_cel_to_far(cel):
    #cel = float(input("Enter a temperature in degree celsius: "))
    f = cel * 9 / 5 + 32
    print(f"The temperature in degree celsius is {f}")
    return f


def convert_far_to_cel(far):
    #far = float(input("Enter a temperature in degree fahrenheit:"))
    c = (far - 32) * 5/9
    print(f"The temperature in degree fahrenheit is {c}")
    return c


if __name__ == '__main__':
    cel = float(input("Enter a temperature in degree celsius: "))
    far = float(input("Enter a temperature in degree fahrenheit:"))
