#Range functions returns a sequence of numbers, starting from0 by default,
#Increments by 1(by default) and stops befopre a specifies number.

seq =range(9)

for i in seq:
     print(i)

for j in range(2,10, 2):# range(start,stop,step)
     print(j)

#QS
# PRINT NUMBER FROM 1 TO 100

for i in range(1, 101):
     print(i) 


n = int(input("ENter the number:"))

for i in range(1,11):
     print(n*i)

#Pass Statement
for el in range(10):
     pass

print("Nothing is executed")

