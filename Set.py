#Set is the collection of unOrdered items and are mutable
#Each Element in the set must be unique & immutable


collection ={1,2,3,4,5,5,6,6,6,6} # Repeated values are ignored by the set 
print(collection)
print(type(collection))

null_set = set() #For creating a empty set


#Methods in Set
# We cannot add list

#Unhasable value means mutable value

data = set()
data.add(4548)
data.add(4548)
data.add(9)
data.add(1)
data.remove(1)
print(data)

#data.clear()  clears all the value

coll = {"Hello", "World", "Mindrisers"}
coll.pop() #Removes a Random Value
print(coll)
 


#Union Method combines both set values and return new one
set1 = {1,6,5,8}
set2 = {4,1,5,8,6,4,9}
newSet = set1.union(set2)
print(newSet)


#Intersection Method' Combines Common value and returns new one

interSection = set1.intersection(set2)
print(interSection)

#Pratice Questions

#You are given a list of subjects for students.
# Assume one classRoom is required for `subject. How many classroom are needed by all students.

subjects = {
     "Python",
     "Python",
     "Python",
     "Java",
     "Java",
     "Java",
     "C++",
     "C++",
     "C",
     "JavaScript"
}
print(subjects)
finalValue = len(subjects)
print(finalValue)


#Wap to enter marks of 3 subjects from the users and store them in a dictionary.
#Start With an empty dictionary and add one by one.Use subject name as key and marks as value.

marks ={}

x = int(input("Enter Phyp : "))
marks.update({"Phyp" :x})

x = int(input("Enter Math:"))
marks.update({"Math" : x})

x = int(input("Enter chem:"))
marks.update({"Chem": x})

print(marks)

# Figure out a way to store 9 and 9.0 as separate values in the set.
#(You can take hepl of built-in data Types)

store ={9,"9.0"}
print(store)