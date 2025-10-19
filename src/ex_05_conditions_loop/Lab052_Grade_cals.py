""" Grade Calculator
write a program that calculates and displays the letter grade
for a given numerical score (ex: A,B,C,D,or F)
based on the following grade scale

A = 90-100
B= 80-89
C= 70-79
D = 60-69
F = 0-59
"""
# user Input is - score --int
# O/p is String - Str -- Which has grades - A, B,C,D, F

score = int(input("Enter the score: ").strip())

"""
if score > 0 and score > 100: 
    print("Enter valid Score")
else:
    print("Let me check")"""

if score >= 90 and score <= 100:  # or 90 <= score <= 100
    print("Your Grade is A")
elif score >= 80 and score <= 89:
    print("Your Grade is B")
elif score >= 70 and score <= 79:
    print("Your Grade is C")
elif score >= 60 and score <= 69:
    print("Your Grade is D")
elif score > 100 or score <= -1:
    print("Enter Valid score in between 0 to 100")
else:
    print("Your Grade is F")



















