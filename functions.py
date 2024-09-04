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

