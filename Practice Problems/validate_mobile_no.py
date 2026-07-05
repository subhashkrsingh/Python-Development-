import re

def validate_mobile_numbers():
    
    try :
        n = int(input())
    except EOFError:
        return
    for _ in range(n):
        number = input().strip()
        
        if re.match(r'^[789]\d{9}$' , number):
            print("YES")
        else:
            print("NO")
        
if __name__ == "__main__":
    validate_mobile_numbers()
