""" Conditional Statements(Decision-Making)

Used when we want to execute certain parts of the code only
if a specific condition is true.

if condition:
   #block of code
elif  another_condition:
    # block of code
else:
    # block of code

Strip() - In built function  which will return a copy of a string with leading
and trailing whitespace removed.

Switch -- There is no Traditional switch statement  like c, java or java script -
but there are several ways to achieve the same functionality

instead of this  in python 3.0 we have  match case

"""


""" Write a program to take user age and let him know , if he can go to club"""

# Step1
Age = int(input("Enter your age \n"))

# Step 2 -logic , age > 21 - he can go  or age < 21 - he cant go

if Age >= 21:
    print("Yes, can go to club")

else:
    print("No, can go to club")


