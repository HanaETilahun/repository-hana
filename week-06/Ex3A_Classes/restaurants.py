class Restaurant:
    """This class stores restaurant information."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type} food.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


restaurant1 = Restaurant("Burger King", "Fast Food")
restaurant2 = Restaurant("Dunkin Donuts", "Coffee and Donuts")
restaurant3 = Restaurant("Subway", "Sandwiches")


restaurant1.describe_rest()
restaurant1.rest_open()

print()

restaurant2.describe_rest()
restaurant2.rest_open()

print()

restaurant3.describe_rest()
restaurant3.rest_open()