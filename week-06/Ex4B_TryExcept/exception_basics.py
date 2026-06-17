# ValueError Example

try:
    age = int("hello")

except ValueError:
    print("ValueError: You entered text instead of a number.")

else:
    print(age)

finally:
    print("Let's try another one...")


# NameError Example

try:
    print(my_variable)

except NameError:
    print("NameError: The variable does not exist.")

else:
    print(my_variable)

finally:
    print("Let's try another one...")


# TypeError Example

try:
    result = "5" + 5

except TypeError:
    print("TypeError: You cannot add a string and an integer together.")

else:
    print(result)

finally:
    print("Let's try another one...")


# SyntaxError Example

try:
    eval("if True print('hello')")

except SyntaxError:
    print("SyntaxError: The code syntax is incorrect.")

else:
    print("No error found.")

finally:
    print("Let's try another one...")


# Another ValueError Example

try:
    number = int("12.5")

except ValueError:
    print("ValueError: Cannot convert decimal text into an integer.")

else:
    print(number)

finally:
    print("Let's try another one...")


# Another TypeError Example

try:
    total = len(100)

except TypeError:
    print("TypeError: len() only works with collections like strings or lists.")

else:
    print(total)

finally:
    print("Let's try another one...")