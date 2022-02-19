"""Dictionary in python are key value pair data structure"""
"""Dictionary is a collection of key-value pairs"""
"""Dictionary is a mutable data type"""
"""Dictionary is an unordered collection of key-value pairs"""


"""Creating a dictionary"""
"""The dictionary is created by using curly braces"""
"""The keys and values are separated by a colon"""
"""The keys and values are separated by a comma"""


"""Creating a dictionary"""

"""There are two ways to create a dictionary"""
"""
1. Using the dict() function
2. Using the dict constructor
"""
"""Example 1: Using the dict constructor"""




student = {"name": "Rogers", "age": 20, "marks": [90, 80, 70]}
student1 = {"Rogers": "Rogers 23 cpga 4.5 marks 90", "Samuel": "Samuel 23 cpga 4.5 marks 90"}

print(student1["Rogers"])
print(student1["Samuel"])
# student = dict(name="Rogers")

"""Methods of dictionary"""
"""
The methods of dictionary are:
1. clear()
2. copy()
3. fromkeys()
4. get()
5. items()
6. keys()
7. pop()
8. popitem()
9. setdefault()
10. update()
11. values()
"""

"""Adding a key-value pair to the dictionary"""

student1["Goeffrey"] = "Goeffrey 23 cpga 4.5 marks 90"


"""Adding items to dictionary from user input"""
student_key = input("Enter the key: ")
student_name = input("Enter the name of the student: ")
student_age = int(input("Enter the age of the student: "))
student_marks = int(input("Enter the marks of the student: "))
student_cgpa = float(input("Enter the cgpa of the student: "))

student1[student_key] = f"Name: {student_name} Age: {student_age} CGPA: {student_cgpa} Marks: {student_marks}"
# student1 = dict(James="James 23 cpga 4.5 marks 90")


print(student1)


"""Viewing items in a dictionary"""

print(f'Student one is - {student1["Goeffrey"]} and another student is - {student1["Samuel"]}')

print(student1)

"""print all the keys in the dictionary"""
print(student1.keys())

"""print all the values in the dictionary"""
print(student1.values())

"""Print all the items in the dictionary"""
print(student1.items())


"""Updating a dictionary"""
# student1 = dict(Rogers="Rogers 23 cpga 4.5 marks 90", Samuel="Samuel 23 cpga 4.5 marks 90")
student1["Goeffrey"] = "Goeffrey 21 cpga 5.0 marks 100"
print(student1)

student1.update({"Goeffrey": "Goeffrey 21 cpga 4.80 marks 100"})
print(student1)

student1.update(Goeffrey="Goeffrey 21 cpga 4.70 marks 100")
print(student1)