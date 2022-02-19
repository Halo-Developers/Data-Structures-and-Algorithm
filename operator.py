"""In python there are 5 types of orerators

    - Arithmetic operators
    - Assignment operators
    - Comparison operators
    - Logical operators
    - Bitwise operators
    - Membership operators

"""


# Arithmetic operators
# Addition operator
"""The are
    -  Addition operator +
    -  Subtraction operator -
    -  Multiplication operator *
    -  Division operator /
    -  Floor Division operator //
    -  Modulus operator %
    -  Exponent operator **
"""

"""Examples:"""

num = 10
num1 = 20

sum = num + num1
print(sum)

dif = num - num1
print(dif)

"""Assignment operators"""
"""These are used to assign values to variables"""
"""They include:
    - Assignment operator =
    - Addition assignment operator +=
    - Subtraction assignment operator -=
    - Multiplication assignment operator *=
    - Division assignment operator /=
    - Floor Division assignment operator //=
    - Modulus assignment operator %=
    - Exponent assignment operator **=
"""
"""Examples:"""

num = 10
num1 = 20

sum = num + num1
print(sum)

sum += num1

print(sum)

sum += 15
print(sum)


"""Comparison operators"""
"""
These are used to compare values
By default this returns true or false

They include:
    - Equal to operator ==
    - Not equal to operator !=
    - Greater than operator >
    - Less than operator <
    - Greater than or equal to operator >=
    - Less than or equal to operator <=

"""

"""Examples:"""

num = 10
num1 = 20

print(num > num1)

num = 10
num1 = 11

print(num != num1)


"""Logical operators"""

"""These are used to combine conditions"""
"""They Include:
    - Logical AND operator and
    - Logical OR operator or
    - Logical NOT operator not

"""
"""Examples:"""

num = 2
num1 = 3

print(num > num1 and num1 > num)
print(num > num1 or num1 > num)


"""Bitwise operators"""
"""These are used to perform bitwise operations"""
"""They Include:
    - Bitwise AND operator &
    - Bitwise OR operator |
    - Bitwise XOR operator ^
    - Bitwise NOT operator ~
    - Left Shift operator <<
    - Right Shift operator >>
"""

"""Examples:"""
num = 2
num1 = 3
num2 = 4
num3 = 5

print(num > num1 & num1 > num)
print(num > num1 | num1 > num)
print(num < num1 ^ num2 >num3)
print(~num)


"""Membership"""

name = "Samuel"

print("z" in name)
