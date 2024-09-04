#Block of Statement that performs a specific task

# a=5;
# b=10;
# sum = a+b
# print(sum)


# function Defination
def calculate(a,b): #parameters
    sum = a +b
    print(sum)
    return sum
calculate(45,34) #This is the argument, Function call

def print_hello():
    print("Hello!")

print_hello()    
print_hello()    


# Finding the average of three numbers
def average(a,b,c):
    avg = a +b + c/3
    print("The average of three numbers is: ", avg)
    return avg

average(10,45,69)

#Built-in Functionss in Python
# Print()
# len()
# type()
# range()

# User Defined Function
# The function written by the user i.e programmer is a user defined 

#Default Parameter:
#Assigning a default value to parameter, which is used when no argument is passed

def parameter(a=1,b=2):
    print("The product of a and b is:",a*b)
    return a*b
parameter()



#Questions

def length():
    str = "Hello"
    print("The length of the string is: ", len(str))
    return len(str)
length()

itemss = ["Milk","Curd","Paneer","Chicken"]

def sortItem(item):
    for items in item:
        print(items,end = "")

sortItem(itemss)
