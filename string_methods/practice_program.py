# validate user input exercise
# 1 name should be less than or equal to 12 characters
# 2 name should not contain any spaces
# 3 name should only contain alphabets

name = input("Enter your name: ")

if len(name)<=12 and name.find(" ") == -1 and name.isalpha():
    print(f"Hello {name}, your name is valid")
else:
    print(f"Hello {name}, your name is invalid")