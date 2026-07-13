a= int(input(f'Enter the number:'))
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except Exception as e:
    print("Invalid input")

print("Some important lines of codes")
print("End of program")