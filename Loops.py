#While Loop
# Loop process is also called Iteration.And the variable is Iterater..
count = 1 # Here count is iterater
while count<=5:
     print("Rajat")
     count += 1

     print("Loop Ended")


#Print numbers from 1 to 100

i = 1
while i <=100:
     print(i)
     i += 1

#qs2
j = 100
while j>=1:
     print(j)
     j-= 1

print("ended")     



#Print multiplication table of a number n
n = int(input("Enter the number:"))
i = 1
while i<=10:
     print(n*i)
     i +=1


#qs4
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
     print(nums[idx])
     idx+=1


#SEARCH FO A NUMBER X IN THIS TUPLE USNIG LOOP
numbers = (1,4,9,16,25,36,49,64,81,100)
x = 49
i = 0
while i < len(numbers):
     if(numbers[i] == x):
          print("Found the number X at index:", i)
          break
     i +=1
      

#Break(terminates the loop) And Continue(terminates execution in the current iteration and 
# continues execution of the loop with the next iteration)

z = 0
while z<=6:
     if(z == 4):
          z+=1
          continue #In this 4 is not executed.(Acts as Skip)
     print(z)
     z+=1


#For Loops
items = ["Milk", "Curds", "Potato", "Cucumber"]

for val in items:
     print(val)



# QAS 1
list = [1,4,9,16,25,36,49,64,81,100]
for val in list:
     print(val)


tup =[1,4,9,16,25,36,49,64,81,100]  # In this case the process is called linear searching.
x = 9  
idx = 0
for el in tup:
     if(el == x):
          print("X is Found At the Index:", idx)
     idx+=1     