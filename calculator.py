operator = input("Enter the operation to be done + ,-,*,/")
num1 = float(input("enter the first number"))
num2 = float(input("enter the second number "));

if(operator == '+' ):
    result = num1 + num2
    print(result)

elif(operator == '-'):
    result = num1 - num2
    print(result)

elif(operator == '*'):
     result = num1 * num2
     print(result)
    
else:
    print(num1 / num2)