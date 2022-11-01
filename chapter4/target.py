# river = 'Mississippi'
# target = input('Input a character to find: ')
# for index in range(len(river)):
#     if river[index] == target:
#         print("Letter found at index: ",index)
#         break
#
# else:
#     print('Letter',target,'not found', river)

river = 'Mississippi'
target = input('Input a character to find: ')
for index, letter in enumerate(river):
    if letter == target:
        print("Letter found at index: ", index)
        break

else:
    print('Letter', target, 'not found', river)
