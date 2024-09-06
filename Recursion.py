# When a function calls itself repeatedly is known as recursion.

def show(n):
   if(n == 0):
      return
   print(n)
   show(n-1)
     

show(5)    



def fact(n):
   if(n == 0):
      return 1
   else:
      return n * fact(n-1)
   
print(fact(4))   