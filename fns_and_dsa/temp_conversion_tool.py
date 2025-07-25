FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
def  convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

Temp = int(input("Enter the temperature to convert: "))
specification = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if specification == "C":
    print(f"{Temp}°C is {convert_to_fahrenheit(Temp)}°F")
elif specification == "F":
    print(f"{Temp}°F is {convert_to_celsius(Temp)}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")