"""Python Operators

Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators
"""
"""      Assignment Operator     """
# +=add,-=subtract,*=multiply,/=float division,//=integer division,%=modulas (it gives reminder),**=exponent
print(565+6595)
print(2-3)
print(2*3)
print(4/2)
print(2/4)
print(4//2)
print(56%5)
print(2**9)
print(2**0.5)
print(round(2**0.5,4))#roundoff
#precedence rule
#():Highest
#exponent:rtl(right to left)
#*,/,//,%:ltr
#+,-:ltr
print(12.5%2)
print(2**3**2)#2**9(rtl)

name="ashwani"
name=" Hii it's"+name
name +="it's"
print(name)





"""Python Comparison Operators

Comparison operators are used to compare two values:
Operator  Name 	Example 
==  	Equal 	x == y 	
!= 	   Not equal 	x != y 	
> 	   Greater than 	x > y 	
< 	   Less than 	x < y 	
>= 	   Greater than or equal to 	x >= y 	
<= 	   Less than or equal to 	x <= y"""

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x<y)
print(x<=y)
print(x>=y)




"""Python Logical Operators

Logical operators are used to combine conditional statements:
Operator 	Description 	Example 	Try it
and  	Returns True if both statements are true 	x < 5 and  x < 10 	
or 	Returns True if one of the statements is true 	x < 5 or x < 4 	
not 	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)"""
x = 5

print(x > 3 and x < 10)
print(x > 3 or x < 10)
print(not(x > 3 and x < 10))




"""Python Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
Operator 	Description 	Example 	Try it
is  	Returns true if both variables are the same object 	x is y 	
is not 	Returns true if both variables are not the same object 	x is not y"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have thew same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content




"""Python Membership Operators

Membership operators are used to test if a sequence is presented in an object:
Operator 	Description 	Example 	Try it
in  	Returns True if a sequence with the specified value is present in the object 	x in y 	
not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y"""

x = ["apple", "banana"]
print("banana" in x)

# returns True because a sequence with the value "banana" is in the list
print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list





"""Python Bitwise Operators

Bitwise operators are used to compare (binary) numbers:
Operator 	Name 	Description
&  	AND 	Sets each bit to 1 if both bits are 1
| 	OR 	Sets each bit to 1 if one of two bits is 1
 ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
~  	NOT 	Inverts all the bits
<< 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost 
bits fall off"""
#!/usr/bin/python

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101 
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)
