class twelve_days:

    @staticmethod
    def christmas_song():
        for i in range(1, 13, 1):
            print('on the ')
            match i:
                case 1:
                    print('first')
                case 2:
                    print('second')
                case 3:
                    print('third')
                case 4:
                    print('fourth')
                case 5:
                    print('fifth')
                case 6:
                    print('sixth')
                case 7:
                    print('seventh')
                case 8:
                    print('eighth')
                case 9:
                    print('ninth')
                case 10:
                    print('tenth')
                case 11:
                    print('eleventh')
                case 12:
                    print('twelfth')

            print('Day of christmas,my true love sent to me')
            for s in range(1, 13, 1):
                match s:
                    case 12:
                        print(' Twelve drummers Drumming ')
                    case 11:
                        print('Eleven pipers piping')
                    case 10:
                        print('Ten lords a-leaping')
                    case 9:
                        print('Nine ladies dancing')
                    case 8:
                        print('Eight maids a -milking')
                    case 7:
                        print('Seven swans a-swimming')
                    case 6:
                        print('Six geese a-laying')
                    case 5:
                        print('Five golden rings')
                    case 4:
                        print('Four calling birds')
                    case 3:
                        print('Three french hens')
                    case 2:
                        print('Two turtle doves, and ')
                    case 1:
                        print(' A partridge in a pear tree ')


if __name__ == '__main__':
    twelve_days.christmas_song()
      