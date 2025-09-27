## Hello Python! ##

# General Build Anythin
# Open Source
# Python packages, also for data science
    #Many applications and fields


# Addition
#print(5+8)

# Substraction
#print(3-7)

# Multiplication
#print(3*5)

# Division
#print(5 / 8)

# Python shell for experimention and code lines to actual answer



## Variables & Types ##
    #Specific, case-sensitive name
    # Call up value through variable name

"""
Other variable types
In the previous exercise, you worked with the integer Python data type:

int, or integer: a number without a fractional part. savings, with the value 100, is an example of an integer.
Next to numerical data types, there are three other very common data types:

float, or floating point: a number that has both an integer and fractional part, separated by a point. 1.1, is an example of a float.
str, or string: a type to represent text. You can use single or double quotes to build a string.
bool, or boolean: a type to represent logical values. It can only be True or False (the capitalization is important!).
"""

# Eg.
height = 1.79
weight = 68.7

bmi = weight / height ** 2

print (68.7 / 1.79 ** 2)

print (bmi)

#Python Types
# float
type(bmi) # 21.44127836209856 float = number with both integer part and a fractional part.

# int
day_of_week = 5

type(day_of_week) # int = integer. For DS youll need more than intes and floats though

# str

x = "body mass index" # string = represents text
type(x)

# bool

z = True # bool = represents True or False condition. Booleans will be very useful in teh future, to perform filtering operations on your data for example.

print(type(z))

# Comments
    #The plus operator behaved differently for different data types. This is a general principal, how the code behaves on the types one is working with
    # Different type = different behaviour

## Excercise Module ##
"""
# Create a variable savings
savings = 100

# Print out savings
print(savings)

# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Print new_savings
print(new_savings)
"""