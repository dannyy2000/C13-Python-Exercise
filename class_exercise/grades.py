def student_grade():

    counter = 1
    while(counter <= 3 ):

       grade = int(input("Enter a grade: "))

       if grade >= 90 and grade <= 100:
        print("A")
        break
       elif grade >= 70 and grade <= 89:
        print("B")
        break
       elif grade >= 50 and grade <= 69:
        print("C")
        break
       elif grade >= 40 and grade <= 49:
         print("D")
         break
       elif grade >= 30 and grade <= 38:
         print("E")
         break
       elif grade < 0 or grade > 100:
         print("Invalid input")
       else:
         print("Zero talent!!!")
         break
       counter+=1


if __name__ == '__main__':
    student_grade()