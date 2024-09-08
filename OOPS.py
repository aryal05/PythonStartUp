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


#The self parameter is a eference to the current instance of the class, and is used to access variables that belonmgs tot he class 

class info:
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
