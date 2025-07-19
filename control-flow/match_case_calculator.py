num1 = int(input("Enter the first number: ").strip())
num2= int(input("Enter the second number: ").strip())
operation = input("Choose the operation (+, -, *, /): ").strip()

match operation:
    case "+":
        print("The result is",num1+num2)
    case "-":
        print("The result is",num1-num2)
    case "*":
        print("The result is",num1*num2)
    case "/":
        if num2==0:
            print("Cannot devide by zero.")
        else:
            print("The result is", num1/num2)
    case default:
        print("You entered incorrect operation, please choose again!")