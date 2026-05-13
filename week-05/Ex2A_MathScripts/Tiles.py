import math

# Room dimensions in feet
length = 10
width = 12

# Tile information
tiles_per_box = 12

# Calculate tiles needed
room_area = length * width
tiles_needed = room_area

# Boxes needed without extra tiles
boxes_needed = math.ceil(tiles_needed / tiles_per_box)

# Add 10% extra tiles
extra_tiles_needed = tiles_needed * 1.10

# Total boxes to buy
total_boxes = math.ceil(extra_tiles_needed / tiles_per_box)

# Output
print("The room area is " + str(room_area) + " square feet")
print("Boxes needed are " + str(boxes_needed))
print("Total boxes to buy with 10% extra are " + str(total_boxes))
total_boxes = math.ceil((length * width * 1.10) / 12)