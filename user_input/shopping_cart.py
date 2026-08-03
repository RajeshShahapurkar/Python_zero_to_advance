item = input("enter the item you want to by: ")
price = float(input("enter the price of the item: "))
quantity = int(input("enter the quantity of items: "))

total= price*quantity
print(f"The total cost for {quantity} {item} is {total}")