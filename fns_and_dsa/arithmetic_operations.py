def perform_operation(num1,num2,operation):
    match operation:
        case "add":
            return num1+num2
        case "subtract":
             return num1-num2
        case "multiply":
             return num1*num2
        case "divide":
             return num1/num2 if num2!=0 else "Division By zero is not Possible"
        case _:
            return "Enter the correct operation among (add, subtract, multiply, divide)"
             


    