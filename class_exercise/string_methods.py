#s = "i want two things in life, loving you and be loved by you"
import string
#print(s.upper())
#print(s.lower())
#print(s.capitalize())
#print(s.title())
#print(s.swapcase())
#print(s.casefold())

#print(s.count("o", 10, 38))
#print(s.find("you"))
#print(s.index("you"))
#print(s.rfind("you"))
#print(s.rindex("you"))
#print(s.find("you",s.find("you") + 1))
#print(s.startswith("I want"))

# binary = '10010100111'
# print(binary.translate(str.maketrans('01', '10')))
# word = input("Enter a word: ")
# key = int(input("Enter the key to code with: "))
# abc = string.ascii_lowercase
# inverse = abc[key:] + abc[:key]
# print(word.translate(str.maketrans(inverse, abc)))

# print('{:>10s} is {:<10d} years old'.format('Bill', 25))
for i in range(5):
    print("{:10d} --> {:4d}".format(i, i**2))