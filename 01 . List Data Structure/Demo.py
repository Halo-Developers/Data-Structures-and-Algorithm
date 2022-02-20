#List comprehension

"""
The concept of list comprehension takes in three parameters
  - expression
  - iteration
  - codition (This usually optional)
  
  syntax of list comprehension
  list_of_numbers_from_1_to_10 = [expression iteration condition]
"""
#example of list comprehension with without condition
list_of_numbers_from_1_to_10 = [number for number in range(11)]

#example of list comprehension with without condition

list1 = [x/2 for x in range(110)]
print(list1)



#example of list comprehension with with condition
names = ["Rogers", "Edgar", "Joan", "Bam", "Hellen", "Angei"]

list_of_names_with_letter_o = [name for name in names if 'o' in name]
print(list_of_names_with_letter_o)

list_of_names_with_letter_e = [name for name in names if 'e' in name.lower()]
print(list_of_names_with_letter_e)

list_names_starting_with_letter_h = [name for name in names if name.lower().startswith('h')]
print(list_names_starting_with_letter_h)
