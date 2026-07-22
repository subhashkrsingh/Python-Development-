# def calculateGmean(a,b):
#     mean=(a*b)/(a+b)
#     return(mean)

# a= int(input("Enter first no.:"))
# b = int(input("Enter second no.:"))

# print(calculateGmean(a, b))
# print ("End of program")



# def is_Greater(a,b):
#     if(a>b):
#         print("First no is greater")
#     else:
#         print("Second no is greater or equal")

# is_Greater(a,b)

# def average(a,b):
#     print("The average is ", (a+b)/2)
# average (7,6)


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is:",sum / len(numbers))
    return sum / len(numbers)

c = average(5,7,4,1)
print(c)