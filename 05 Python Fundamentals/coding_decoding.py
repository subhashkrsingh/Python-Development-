import random
import string



def random_chars():
    return ''.join(random.choice(string.ascii_letters) for _ in range(3))

def encode(word):
    if len(word) >= 3 :
        first= word[0]
        word = word[1:]+ first
        word = "hgi"+word+"wer"
        return(word)
    else:
        return(word[::-1])
    

def decode(word):
    if len(word) < 3:
        return word[::-1]
    else:
        word = word[3:-3]

        word = word[-1]+ word[:-1]

        return word
    

choice = input("Enter E for Encode or D for Decode: ").upper()
text = input("Enter the message: ")

words= text.split()

result=[]

if choice == "E":
    for word in words:
        result.append(encode(word))
    print("Encoded Message:")
    print(" ".join(result))

elif choice == "D":
    for word in words:
        result.append(decode(word))
    print("Decoded Message:")
    print(" ".join(result))

else:
    print("Invalid Choice!")
