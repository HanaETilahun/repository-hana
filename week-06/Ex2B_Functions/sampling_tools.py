import random

products = [
    "Laptop", "Monitor", "Keyboard", "Mouse", "Webcam",
    "Headset", "Docking Station", "USB Hub", "Desk Lamp", "Surge Protector"
]

product_of_day = random.choice(products)
print(f"Product of the Day: {product_of_day}")

survey_products = random.sample(products, 3)
print(f"Survey products: {survey_products}")

random.shuffle(products)
print(f"Shuffled products: {products}")

daily_transactions = random.randint(50, 300)
print(f"Daily transaction count: {daily_transactions}")