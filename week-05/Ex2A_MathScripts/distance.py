import math

# Define coordinates
x1 = 2
y1 = 3
x2 = 6
y2 = 7

# Calculate distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output
print("Point 1: (" + str(x1) + ", " + str(y1) + ")")
print("Point 2: (" + str(x2) + ", " + str(y2) + ")")
print("The distance between the points is " + str(distance))