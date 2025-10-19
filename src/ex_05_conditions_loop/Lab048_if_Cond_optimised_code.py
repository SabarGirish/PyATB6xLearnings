""" Write a program to take user age and let him know ,
if he can go to club"""

# Updated and optimised code

# Strip - here  we can enter   age 21  , remove the extra saoces from input function


# Step1
Age = int(input("Enter your age \n").strip())

#Nested if statement - covers few edge cases which has less than 0
# or more than human life age


if Age <= 0 or Age >= 130:
    print("Enter Valid age")
else:
    if Age >= 21:
        print("Yes, can go to club")

    else:
        print("No, can go to club")


