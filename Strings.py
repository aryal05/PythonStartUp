#Strings
#Concatination
str1 = "Hello"
str2 = "World"
print(str1 + str2)

#Length of Str
print(len(str1))


#Indexing starts from 0
print(str1[0])

#Slicing Accessing parts of a string
#str[starting_idx : ending_idx] ending idx is not included

str = "Mindrisers"
print(str[1:5])

#Negative indexing
print(str[-4:-1])

#String Functions

str3 = "I am studying python and a hacker and Security analyst."
print(str3.endswith("thon"))
#Replace
print(str3.replace("a", "o"))# "old value", "new value"

#Find
print(str3.find("o"))

# Count
print(str3.count("and"))

# Wap to input users first name & print its length

name = input("Enter First Name:")
print(len(name))