
pi = 3.14
radius = int(input("Enter R: "))
areaOfCircle = pi * radius**2
print("areaOfCircle = ", areaOfCircle)

physics = int(input("Enter the physics Marks:"))
maths = int(input("Enter the Maths Marks:"))
computer = int(input("Enter the Computer Marks:"))
totalMarks = physics + maths + computer
percentage = (totalMarks)/300*100
print("percentage is = ",percentage)