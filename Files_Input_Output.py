#Python can be used to perform operations on a file.(read and write data)

#Types of file
#Text Files (.txt, .docx, .log etc)

#Binary Files (.mp4, .jpg, .exe etc)

# To read all the lines in the file
f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

# To read the first line
f = open("demo.txt", "r")
line = f.readline()
print(line)
f.close()


#Writing in file

write = open("demo.txt", "w")
write.write("This is the changed file due to writing method") # This changes entire text of demo.txt file and add write.write(" this line to the existing text.")
write.close()



# Writing in file using append
append = open("demo.txt", "a")
append.write("\nThis is appended text in the existing file.")
append.close()


# To Create new txt file in the folder
new_file = open("new_demo.txt", "w")
new_file.write("This is a new file created using python")
new_file.close()

# To do reading and writing at the same time
read_write = open("demo.txt", "r+")
data = read_write.read()
read_write.write("\nThis is the changed file due to read write method ")
read_write.close()


#With Syntax
with open("with_demo.txt", "w+") as write_with:
    write_with.write("This is the changed file due to write method using with syntax")
    data = write_with.read()
    print(data)
# at the end we dont need to close the code manually if we usse with syntax.


# Deleting the file
# Deleting file using os module
# import os
# os.remove("domo.txt")

    
#Practice 

# Creating new file and then writting in it.
with open("practice.txt", "w") as pract:
    pract.write("This is the practice file")
    pract.write("\nJava")
    print("File written successfully.")
# Reading and overWriting the data
with open("practice.txt", "r+") as pract:
    data = pract.read()
# Replacing Java with Python
new_data = data.replace("Java","Pythom")
# Uploading the new replaced file.
with open("practice.txt", "w") as pract:
  pract.write(new_data)
print(new_data)    