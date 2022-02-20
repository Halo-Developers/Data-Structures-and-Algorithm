#List comprehension

list1 = [x/2 for x in range(110)]
print(list1)


names = ["Rogers", "Edgar", "Joan", "Bam", "Hellen", "Angei"]

list_of_names_with_letter_o = [name for name in names if 'o' in name]
print(list_of_names_with_letter_o)

list_of_names_with_letter_e = [name for name in names if 'e' in name.lower()]
print(list_of_names_with_letter_e)

list_names_starting_with_letter_h = [name for name in names if name.lower().startswith('h')]
print(list_names_starting_with_letter_h)