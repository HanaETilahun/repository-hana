# Create a list
foods = ["tacos", "ramen", "jerk chicken", "injera", "pierogi"]

# Print numbered list
for index, food in enumerate(foods, start=1):

    # Check for first item
    if index == 1:
        print(f"{index}. {food} <- top pick!")
    else:
        print(f"{index}. {food}")

print("\nReverse Order:\n")

# Reverse order bonus
reversed_foods = list(reversed(foods))

for index, food in enumerate(reversed_foods, start=1):
    print(f"{index}. {food}")