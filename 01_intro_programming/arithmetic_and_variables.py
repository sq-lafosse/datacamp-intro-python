"""
# =========================================
#           Arithmetic and Variables
# =========================================
"""

# --------- Printing ---------

print("Hello, World!")  # Prints str.

# === Arithmetic ===

print(1 + 2)      # Addition
print(2 - 1)      # Substraction
print(2 * 2)      # Multiplication
print(9 / 3)      # Division
print(3 ** 2)     # Exponent

"""
+---------------+----------+------------------+
| Operation     | Symbol   | Example          |
+---------------+----------+------------------+
| Addition      | +        | 1 + 2 = 3        |
| Subtraction   | -        | 5 - 4 = 1        |
| Multiplication| *        | 2 * 4 = 8        |
| Division      | /        | 6 / 3 = 2        |
| Exponent      | **       | 3 ** 2 = 9       |
+---------------+----------+------------------+
"""


# --- Comments ---

# We use comments to annotate what code is doing. They help other people to understand your code, and they can also be helpful if you haven't looked at your own code in a while. So far, the code that we have written is very short, but annotations become more important when you have written a lot of code.


# --- Variables ---

test_var = 4 + 5 

print(test_var)  # Prints 9


# --- Using Multiple Variables ---

# Create variables
num_years = 4
days_per_year = 365 
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)

# --- Debbuging ---

# One common error when working with variables is to accidentally introduce typos. For instance, if we spell hours_per_day as hours_per_dy, 
# Python will error with message NameError: name 'hours_per_dy' is not defined.





# >>> Exercise: Arithmetic and Variables <<<























