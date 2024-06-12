studNam = ["Ram", "Hari", 85, "David Millar", "MOhomad Amir"]
print(studNam[0])
studNam[0] = "Shyam" 
print(studNam)
# str = "hello"
# print(str[0])
# str[0] = "Y" # this line of code cannot be done in python because strings are immutable
# List Methods
list = [25,3,4,5]
list.append(4)  # Adds one element at the end.
print(list)

list.sort() #Sorts in Ascending Order.
print(list)


list.sort(reverse=True) #Sorts in Desending Order
print(list)

list.reverse() #Reverse List [5,4,3,25]
print(list)

list.remove(4) # Remove first 4 that is in the list
print(list)

list.pop(2) # Deletes according to the  index we have entered



# Now Tuples
#Tuple is immutable Data Type that means we cannot assign new value 

tup = (45,87,26,26,19)
print(tup)
print(type(tup))


#Tuple Methods
tp = (12,89,74,56)
# print(tp.index(0))
print(tp)

print(tup.count(26)) # Count Total Occurrences



#Practice Questions
#WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3FAV MOVIES AND STORE THEM IN A LIST..

movies = []
mov1 = input("Enter first Movie:")
mov2 = input("Enter Second Movie:")
mov3 = input("Enter Third Movie:")


movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)


#WAP TO CHECK IF A LIST CONTAINS A PALIDROME OF ELEMENTS. (HINTS: USE COPY () METHOD)

num1 = [1,2,3,1]

copy_num1 =num1.copy()
copy_num1.reverse

if(copy_num1 == num1):
     print("Palindrome")
else:
     print("Not A Palindrome")



grade = ["C", "D", "A", "A", "A", "B", "B"]
grade.sort()
print(grade)