# Write a Program to calculate the area of a circle given its radius
# using the formula  Area  = PI *  r**2 (pi = 3.14)

radius = 10.0

 # Inp r is in float
 #O/P -String formated output  of area

Area = 3.141592653589793 * radius ** radius
print(Area)


Area = 3.141592653589793 * (radius ** radius)
print(Area)



Area = 3.141592653589793 * (pow(radius, 2))
print("Area of circle:", Area)

# String Data Formatting -- This is only for float ,
# Python  f- strings, formatted string  literals
print(f"Area of circle is -> {Area:.2f}")

# here .2f is  the decimal point is only 2 , f is formatting






