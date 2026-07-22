a = int(input("Enter a number between 0 to 10:"))

match a:
    case 1:
        print("you won an adapter")
    case 7:
        print("you won $7")
    case 5:
        print("yoou won an iphone")
    case _:
        print("Better luck next time.") 