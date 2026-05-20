class Restaurant:
    """This class stores restaurant information."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type} food.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        customers = int(input("How many customers served today? "))
        self.number_served += customers

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    def customer_rating(self):
        while True:
            rating_input = input("How would you rate your experience today on a scale of 1-5? ")

            try:
                rating = int(rating_input)

                if rating >= 1 and rating <= 5:
                    self.customer_ratings.append(rating)
                    average_rating = sum(self.customer_ratings) / len(self.customer_ratings)

                    print(f"Your rating was {rating}. The average rating for this restaurant is {average_rating:.2f}")
                    break
                else:
                    print("Please enter a whole number from 1 to 5.")

            except ValueError:
                print("Invalid input. Please enter a whole number from 1 to 5.")


restaurant1 = Restaurant("Burger King", "Fast Food")
restaurant2 = Restaurant("Dunkin Donuts", "Coffee and Donuts")
restaurant3 = Restaurant("Subway", "Sandwiches")

restaurant1.describe_rest()
restaurant1.rest_open()
restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()
restaurant1.customer_rating()
restaurant1.customer_rating()

print()

restaurant2.describe_rest()
restaurant2.rest_open()
restaurant2.print_num_served()
restaurant2.add_num_served()
restaurant2.add_num_served()
restaurant2.print_num_served()
restaurant2.customer_rating()
restaurant2.customer_rating()

print()

restaurant3.describe_rest()
restaurant3.rest_open()
restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()
restaurant3.customer_rating()
restaurant3.customer_rating()