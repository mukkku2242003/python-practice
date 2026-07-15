number = int(input("Enter your number: "))

if number == 0:
    print("Zero is neither Even nor Odd")

elif number > 0:

    if number % 2 == 0:
        print(f"{number} is a Positive Even Number")
    else:
        print(f"{number} is a Positive Odd Number")

else:

    if number % 2 == 0:
        print(f"{number} is a Negative Even Number")
    else:
        print(f"{number} is a Negative Odd Number")

