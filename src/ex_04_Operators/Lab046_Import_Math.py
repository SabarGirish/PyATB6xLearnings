import math

print(math.pi)
print(math.e)
print(math.pow(2, 3))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))

Radius = int(input("Enter radius: "))  # radius =10

Area = math.pi * math.pow(Radius, 2)
print(f"Area of circle is {Area:.3f}")   #Area of circle is 314.159

# Here Area is in flot converting into String
