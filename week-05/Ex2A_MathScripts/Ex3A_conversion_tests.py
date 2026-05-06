# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

#Define the following variables:
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '
# Original variables
a = " 101.1 "
b = "55"
c = "402 Stevens"
d = "Number 5 "

# --- Transformations ---

# a
a_int = int(float(a))   # works: convert to float first, then int
a_float = float(a)      # works

# a_error = int(a)  
# ValueError: invalid literal for int() because "101.1" is not a whole number

# b
b_int = int(b)          # works
b_float = float(b)      # works

# c
# c_int = int(c)
# ValueError: invalid literal for int() because string has letters

# c_float = float(c)
# ValueError: cannot convert text with letters to float

# d
# d_int = int(d)
# ValueError: contains text and spaces

# d_float = float(d)
# ValueError: contains text and spaces

# --- Print values and types ---

print(a, type(a))
print(a_float, type(a_float))
print(a_int, type(a_int))

print(b, type(b))
print(b_int, type(b_int))
print(b_float, type(b_float))

print(c, type(c))

print(d, type(d))

# --- Observations ---
# a: can convert to float, but not directly to int → must use int(float(a))
# b: converts easily to both int and float
# c: cannot convert to int or float because it contains letters
# d: cannot convert to int or float because it contains words