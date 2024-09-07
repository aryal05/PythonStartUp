#Python can be used to perform operations on a file.(read and write data)

#Types of file
#Text Files (.txt, .docx, .log etc)

#Binary Files (.mp4, .jpg, .exe etc)

f = open("demo.txt", "r")

data = f.read()

print(data)
print(type(data))
f.close()