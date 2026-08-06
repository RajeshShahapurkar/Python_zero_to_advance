weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K/P): " )

if unit == "K":
    weight = weight * 2.20462
    unit = "Lbs."
    print(f"your weight is {weight} {unit}")
elif unit == "P":
    weight = weight / 2.20462
    unit = "Kgs."
    print(f"your weight is {weight} {unit}")
else:
    print(f"{unit} was not valid")

