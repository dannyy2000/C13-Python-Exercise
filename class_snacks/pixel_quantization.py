def pixel_quantization(pixel):

    for counter in range(len(pixel)):

        result = pixel[counter]

        if 0 <= result <= 20:

            pixel[counter] = 10

        elif 21 <= result <= 40:

            pixel[counter] = 30

        elif 21 <= result <= 40:

            pixel[counter] = 30

        elif 41 <= result <= 60:

            pixel[counter] = 50

        elif 61 <= result <= 80:

            pixel[counter] = 70

        elif 81 <= result <= 100:

            pixel[counter] = 90

        elif 101 <= result <= 120:

            pixel[counter] = 110

        elif 121 <= result <= 140:

            pixel[counter] = 130

        elif 141 <= result <= 160:

            pixel[counter] = 150

        elif 161 <= result <= 180:

            pixel[counter] = 170

        else:

            pixel[counter] = 190

    return pixel


if __name__ == '__main__':
    pixels = [15, 18, 22, 27, 44, 98, 183, 195, 179, 164, 148, 139, 111, 75, 86]

    print(pixel_quantization(pixels))