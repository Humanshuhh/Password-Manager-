num = int(input("enter an number between 1 - 10"))

while num < 1 or num > 10 :
    print(f"your number {num} is not valid");
    num = int(input("enter an number between 1 - 10"))

    print(f"Your number is {num}")