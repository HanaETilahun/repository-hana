# 1. Create tuples
candies = ("gummy bears", "lollipops", "jelly beans")
flavors = ("strawberry", "mango", "blue raspberry")

# 3. Create a set of combinations
candy_combinations = set()

candy_combinations.add(candies[0] + " - " + flavors[1])
candy_combinations.add(candies[1] + " - " + flavors[2])
candy_combinations.add(candies[2] + " - " + flavors[0])

# 4. Print output
print("Today’s candy options include:")
print(candy_combinations)

# 5. Print multiple times
print(candy_combinations)
print(candy_combinations)
#What you’ll notice:
#The order changes or looks random each time you print
#That’s because a set is unordered (it doesn’t keep items in a fixed order)