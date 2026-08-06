unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (temp * 9/5) + 32
    unit = "Fahrenheit"
    print(f"The temperature is {temp} {unit}")
elif unit == "F":   
    temp = (temp - 32) * 5/9
    unit = "Celsius"
    print(f"The temperature is {temp} {unit}")
else:
    print(f"{unit} was not valid")