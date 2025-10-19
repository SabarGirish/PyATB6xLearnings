# Ternary Operator  -- if-else statement -- One liner Ternary Operator

x = 10
y= 20

print("x is greater than y " if x > y else "x is less than y")

#This is equal to "
""" if x>y:
    print("x is greater than y")
else:
    print("x is less than y") """

user_age = input("Enter your age: ")

if int(user_age) > 18:
    print("Your age is not young")
else:

    print("Your age is too young")


user_age = int(input("Enter your age: "))
print("Your age is not young" if user_age >=  18 else "Your age too young")

