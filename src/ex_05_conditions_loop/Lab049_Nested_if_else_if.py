
a = 19
if a == 10:
    print("Hello World")
else:
    print("Not Hello")

# Find the number is even or odd

num = int(input("Enter your number \n").strip())

if num >= 0:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative number")

# we can write short one liner conditions using ternary operator
if num >= 0:
    print("Even"if num % 2 == 0 else "Odd")
else:
    print("Negative number")







