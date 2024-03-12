print("\nGrade Calculator\n")
marks = int(input("Enter your marks to see grade: "))

if marks <= 39:
    print("F   Grade Point: 0.00")
elif 39 < marks <= 44:
    print("D   Grade Point: 2.00")
elif 44 < marks <= 49:
    print("C   Grade Point: 2.25")
elif 49 < marks <= 54:
    print("C+  Grade Point: 2.50")
elif 54 < marks <= 59:
    print("B-  Grade Point: 2.75")
elif 59 < marks <= 64:
    print("B   Grade Point: 3.00")
elif 64 < marks <= 69:
    print("B+  Grade Point: 3.25")
elif 69 < marks <= 74:
    print("A-  Grade Point: 3.50")
elif 74 < marks <= 79:
    print("A   Grade Point: 3.75")
else:
    print("A+  Grade Point: 4.00")