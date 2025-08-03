def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        
    try:
        numerator= float(numerator)
        denominator = float(denominator)
    except ValueError:
        print("Please enter numeric values only.")
    
        