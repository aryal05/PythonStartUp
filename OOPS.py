#To Map with real world scenarios, we started using objects in code which is called Object-Oriented Programming (OOP).

#Class And Object in Python

#Class is a blueprint for creating an object. It defines the characteristics and behavior of an object.

#Creating Class
class Car:
    # name = "lambo"
    color = "red" 
    speed = 200

#Creating Object
my_car = Car()
print(my_car.color)


#Constructor
#All classes have a function called __init__(), which is always called when an object is created from a class.
# The __init__() method can take in parameters, which are assigned to instance variables and are used 
# to define the properties of the class.\


#The self parameter is a reference to the current instance of the class, and is used to access variables that belonngs to the class 

class info:
    college_name = "college"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Adding stud in database")
infomation = info("Rajat",99)        
print(infomation.name)
print(infomation.marks)



infomation2 = info("Adit",90)        
print(infomation2.name)
print(infomation2.marks)


#Class And Instance Attributes
 #Class.attr
 #object.attr 

 #And always object attr > class attr


# Methods
#Methods are fucntions that belongs to object

#Crreating Class
class stud:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello, my name is " + self.name)
#Creating Object    
s = stud("Rajat")
s.hello()
      

#Question
# create student class that takes name and marks of 3 subjects as arguments in constructor
# Then create a method to print the average


class student:
    def __init__(self, name, marks):
        self.name=name
        self.marks = marks

    def avg_marks(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        print("Hello", self.name, "Your Average Score is:",sum/3)    




s1 = student("AsP singh",[98,99,97])

s1.avg_marks()






# Static Methods are those parameters that don't use delf parameter.

class static:
    @staticmethod # This is also called decorator which allows us to  wrap another function in order to,
                  # extent the behaviour of the wrapped function,  without permanently modifying it.

    def college():
        print("This is a static method. It belongs to the class, not an instance of the class.")
    
# You can call a static method without creating an instance of the class
static.college()
                




#Abstration 
#Hiding the implementation details of a class and only showinf the essential features to the user.






#Encapsulation
#Wrapping data and functions into a single  unit.

