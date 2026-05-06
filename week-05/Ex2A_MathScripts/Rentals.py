import math

# Number of people
people = 40  # example

# Van details
seats_per_van = 15
cost_per_van = 250

# Calculate vans needed
vans_needed = math.ceil(people / seats_per_van)

# Total cost
total_cost = vans_needed * cost_per_van

# Cost per person
cost_per_person = total_cost / people

# Output
print("Number of people: " + str(people))
print("Vans needed: " + str(vans_needed))
print("Total cost: $" + str(total_cost))
print("Cost per person: $" + str(cost_per_person))