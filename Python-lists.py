"""Python Lists
Python Collections (Arrays)

There are four collection data types in the Python programming language:

    List: is a collection which is ordered and changeable. Allows duplicate members.
    Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
    Set: is a collection which is unordered and unindexed. No duplicate members.
    Dictionary: is a collection which is unordered, changeable and indexed. No duplicate members.

When choosing a collection type, it is useful to understand the properties of that type. Choosing 
the right type for a particular data set could mean retention of meaning, and, 
it could mean an increase in efficiency or security."""




"""List

A list is a collection which is ordered and changeable. In Python lists are written with square brackets."""

thislist = ["apple", "banana", "cherry"]
print(thislist)


"""Access Items in list

You access the list items by referring to the index number:"""

thislist = ["apple", "banana", "cherry"]
print(thislist[1])




"""Change Item Value in list
To change the value of a specific item, refer to the index number:"""
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)




"""Loop Through a List

You can loop through the list items by using a for loop:"""

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 
  
  
  
  
  """Check if Item Exists in list

To determine if a specified item is present in a list use the in keyword:"""
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
    print("hii")



"""List Length

To determine how many items a list has, use the len() method:"""

thislist = ["apple", "banana", "cherry"]
print(len(thislist))



"""Add Items in list

To add an item to the end of the list, use the append() method:"""

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To add an item at the specified index, use the insert() method:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)



"""Remove Item

There are several methods to remove items from a list:"""

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)



""" The pop() method removes the specified index, (or the last item if index is not specified):"""
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#"""The del keyword removes the specified index:"""
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) #this will cause an error because you have succsesfully deleted "thislist".



#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


"""The list() Constructor

It is also possible to use the list() constructor to make a list."""
thislist = list(("apple", "banana", "cherry"))
print(thislist)



"""copy() Method
Copy the fruits list:"""

fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)
"""The copy() method returns a copy of the specified list.
Syntax:list.copy()
"""


#The count() method returns the number of elements with the specified value.
#Syntax:list.count(value)
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)
#Another example:
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
y = fruits.count(9)
print(y)



#The extend() method adds the specified list elements (or any iterable) to the end of the current list.
#Syntax:list.extend(iterable) 
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

#Another Example
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)


#The index() method returns the position at the first occurrence of the specified value.
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

#Another example
fruits = [4, 55, 64, 32, 16, 32]
y = fruits.index(32)
z=fruits.count(32)
print(y)
print(z)
#Note: The index() method only returns the first occurrence of the value.


#The reverse() method reverses the sorting order of the elements.
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
#Syntax:list.reverse() 


#The sort() method sorts the list ascending by default.
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
num=[56,2,7,8,6,5,4,2]
num.sort()
print(num)
print(cars)
#You can also make a function to decide the sorting criteria(s)
#Syntax:list.sort(reverse=True|False, key=myFunc)
#Example :Sort the list decending
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)




#Sort a list of dictionaries based on the "year" value of the dictionaries:
def myFunc(e):
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)


"""#Sort the list by the length of the values and reversed:"""
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)
