

i = (1)
item = (1,)
items = (1,2,3)
print(type(i))
print(type(item))
print(type(items))

list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, "Rogers"]
tuple1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, "Rogers")

print(list1)
print(tuple1)

import sys
import timeit

#Testing for the memory size of the list and tuple
print(f"The memory size of the tuple is {sys.getsizeof(tuple1)} bytes")
print(f"The memory size of the list is {sys.getsizeof(list1)} bytes")


#Testing for the time taken to create the list and tuple
print(f"The time taken to create the tuple is {timeit.timeit('(1,2,3,4,5,6,7,8,9,10)', number=1000000)} seconds")
print(f"The time taken to create the List is {timeit.timeit('[1,2,3,4,5,6,7,8,9,10]', number=1000000)} seconds")


# escape sequence \

print("Rogers is a goodman \"he's\" likes coding")

'Rogers is a goodman "he\'s" likes coding'

# 'Rogers is a goodman he"s likes coding'