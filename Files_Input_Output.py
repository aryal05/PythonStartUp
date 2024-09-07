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


