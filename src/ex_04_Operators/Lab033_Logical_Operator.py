""" Logical Operators

And Gate

A, B , Z  is result

A - 0,and  B-0 is result 0
A - 1 and B-1 is result 1
A - 0 and  B-1 is result 0
A - 1 and  B-0  is result 0

When Both of them is False , it is always False
When Both of them is True , it is always True
When any of them is False , it is always False


Or Gate

A - 0,Or  B-0 is result 0
A - 1 Or B-1 is result 1
A - 0 Or  B-1 is result 1
A - 1 Or  B-0  is result 1

 When Both of them is False , it is always False
 When Both of them is True , it is always True
 When any of them is True  , it is always True

1. And  - True if both are true - true and false - false
2. Or  - True if both are true - true or  false - True
3.Not - Reverses the result  -- Not True  -- False ,
       Not false is True

 """

a = 5
b= 10

print(a > 0 and b > 0)  # True
print(a > 0 or  b < 0)  #True
print(not a > 0)  # False

print(not b > 0) #False

