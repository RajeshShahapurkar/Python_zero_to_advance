num1=int(input("Emter the first number: "))
num2=int(input("Emter the second number: "))

operator=input("Enter the operation to perform(+,-,*,/,%): ")

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    if num2==0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num1/num2)
elif operator=="%":
    if num2==0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num1%num2) 
        
