print("\nGPA Calculator, Spring 2023\n")

tCourse = int(input("Total Course: "))
print("\nEnter each course name with credit and result\n")
course = []
credit = []
result = []
i = 1
while i <= tCourse:
    i += 1
    course.append(input("Course Name: "))
    credit.append(input('Credit: '))
    result.append(input('Result: '))


print(course, credit)
