# hypotenouse of right angled triangle
import math
a=float(input("Enter the first side of triangle: "))
b=float(input("Enter the second side of triangle: "))
hypotenuse= math.sqrt(pow(a, 2)+pow(b, 2))
print(f"The hypotenuse of triangle with sides {a} and {b} is {round(hypotenuse)}")