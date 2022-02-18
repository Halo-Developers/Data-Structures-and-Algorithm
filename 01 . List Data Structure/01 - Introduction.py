"""
List are Mutable Data Structure
List is a collection of items in a particular order

"""

# defining a list
list1 = [1, 2, 3, 4, 5]
#print out list elements
print(list1)

#findout what is the type of data structure I am using
print(type(list1))


# adding elements to the list
list1.append(6)
print(list1)


# removing elements from the list
list1.remove(6)
print(list1)


# removing elements from the list
list1.pop(0)
print(list1)


# extending the list
list1.extend([7, 8, 9])
print(list1)

#make copy of the list
list2 = list1.copy()
print(list2)

"""List comprehension"""
#defining a comprehensive list systanx
"""list_of_item = [expression iteration condition(This is optonal)]"""

# list comprehension
list3 = [i for i in range(10)]
print(list3)

