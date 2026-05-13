print('Hello world!')
message = 'Hello world!'
print(message)
# hello world print twice because we command it to print 2 times
# (It prints twice because you told Python to print the same thing two times)
# Displaying dollars and cents
dollars = 3
cents = 0.50

print(dollars + cents)

#show like money (3.50), use this:
print(f"{dollars + cents:.2f}")
# Observation: The result is 3.5 instead of 3.50 because Python removes trailing zeros in decimal numbers.

dollars = 3
cents = 0.50

print(dollars + cents)

# Update cents
cents = cents + 0.25

# Print new result
print(dollars + cents)

# String variables
d_str = '3 dollars'
c_str = '50 cents'

# Combine with a space in between
print(d_str + " " + c_str)