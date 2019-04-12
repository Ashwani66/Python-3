"""Python Strings
String Literals

String literals in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

Strings can be output to screen using the print function. For example: print("hello").

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. However, 
Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be 
used to access elements of the string."""
#Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])
#Substring. Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])



#The strip() method removes any whitespace from the beginning or the end:
a = "        ------Hello, World! ----      "
print(a.strip())

#The len() method returns the length of a string:
a = "Hello, World!"
print(len(a))

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())


#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 

#String concatination
first_name="Ashwani"
last_name="Singh"
full_name=first_name+ " "+last_name
print(full_name)
#print(first_name+3) is invalid
print(first_name+str(3232))#no error
print(last_name+"6261720300")
print(first_name*5)


#String Formatting
name,age="ashwani",19
print("hello {} your age is {}".format(name,age))#python 3
print(f"Hello {name} Your age is {age+4}")#python 3.x



#string indexing
lang="python"
print(lang[3])


lang="Ashwani"
#string slicing/selecting subsiquences
#syntax:[start arument : stop argument]
print(lang[0:3])
print(lang[2:5])
print(lang[-3:6])
print(lang[:])
print(lang[2:])
print(lang[:3])

# ask user name and  print back user name in reverse order
#Note:- try to make your pgm in 2 lines using string formatting

name=input("enter ur name:")
reverse=name[-1::-1]
print(f"reverse of ur name is {reverse}")

