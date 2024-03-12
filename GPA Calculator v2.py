print("\nGPA Calculator, Spring 2023\n")
tCourse = int(input("Total Course: "))
print("Enter each course credit with result")
result = 0; credit = 0; tCredit = 0
GPA = 0; gpa = 0
i = 1
while i <= tCourse:
    i += 1
    credit = int(input("Credit: "))
    result = float(input('Result: '))
    tCredit += credit
    gpa += credit * result

GPA = round(gpa / tCredit, 2)
print("\nGPA of this Semester is: ", GPA)
