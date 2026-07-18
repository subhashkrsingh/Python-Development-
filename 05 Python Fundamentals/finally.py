def func1(): 
   
   try:
       l = [1,4,5,8,3]
   
       i = int(input("Enter the index: "))
   
       print(l[i])
       return 1
   
   except:
        print("Some error occurred")
        return False

   finally:
      print("I am always Executed")
x = func1()
print(x)



