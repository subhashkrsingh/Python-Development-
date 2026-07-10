#n= int(input("Enter a number:"))
# def factorial (n):
#     if (n==0 or n==1):
#         return 1 
#     else:
#         return n*factorial(n-1)
# print(factorial(4))
# print(factorial(5))
# print(factorial(6))
# 6*factorial(5)
# 6*5*factorial(4)
# 6*5*4*factorial(3)
# 6*5*4*3*factorial(2)
# 6*5*4*3*2*factorial(1) , n=1 it returns 1


#Fibonacci Sequence
# f0 = 0
# f1 = 1
# f2 = f(1) + f(0)
# f3 = f2 + f1
# f(n) = f(n-1) + f(n-2)

def print_fibonacci_iterative(n):
    # Initialize the first two terms
    a, b = 0, 1
    
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print(f"Fibonacci sequence up to {n} term: {a}")
    else:
        print("Fibonacci sequence:")
        for _ in range(n):
            print(a, end=" ")
            # Update values simultaneously
            a, b = b, a + b
        print() # New line

# Change this value to get more or fewer terms
num_terms = 20
print_fibonacci_iterative(num_terms)
