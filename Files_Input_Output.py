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

    write_with.close()
    
