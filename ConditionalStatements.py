# if-elif-else are the (syntax)
age = 20
if(age>15): print("You are eligible to vote")

light = "green"
if(light == "red"):
     print("Stop your Vechicle.")
elif(light == "green"):
     print("You can go.")
elif(light == "yellow"):
     print("Look And Go..")     


# Wap to check if a number is Odd Or Even

num = int(input("Enter the Number:"))
if(num %2 == 0 ):
     print("The number you have entered is: ", num, "Which is a even number.")
else:("Entered number is odd:", num )     

a = int(input("Enter first num:"))
b = int(input("Enter second num:"))
c = int(input("Enter Third num:"))
d = int(input("Enter Fourth num:"))

if(a>=b and a>=c):
     if(a>=d):
          print("First number is the largest number:", a)
elif(b>=c):
     print("Second number is the largest:", b)
elif(c>=d):
     print("Third number is the largest:", c)
else:
     print("Fourth number is the largest:", d)


#WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7

x = int(input("Enter the multiple for 7:"))
if(x %7 == 0):
     print("Multiple of 7.")
else:
     print("Not a multiple of 7.")     
