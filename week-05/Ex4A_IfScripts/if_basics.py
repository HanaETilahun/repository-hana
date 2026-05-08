x = 100
y = 20

# a
if x / y == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("are the variables set up correctly?")

# b
if x * y == y:
    print("now x times y is y")
    x = 10
else:
    print("Whoops, x equals the value of x")

# c
if x < y:
    print("x is less than y")
    x = x * 2
else:
    print("uh oh, x is not less than y")

# d
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

# e
print(f"The final value of x is {x} and the final value of y is {y}")

# pay_rules.py

pay_rate = float(input("Enter pay rate: "))
hours_worked = float(input("Enter hours worked: "))

# Regular pay
if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked

# Overtime pay
else:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

    gross_pay = regular_pay + overtime_pay

print(f"Gross pay: ${gross_pay:.2f}")