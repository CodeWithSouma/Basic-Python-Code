def large_num(num1,num2):
    if num1>num2:
        return "number1 large number"
    elif num1<num2:
        return "number2 large number"
    else:
        return "numbers are equals"
    
while True:
    num1=int(input("enter first number: "))

    num2=int(input("enter second number: "))

    print(large_num(num1,num2))