# 1. Create dictionary
contact_info = {
    "name": "Hana Tilahun",
    "address": "123 Main St",
    "city": "Silver Spring",
    "state": "MD",
    "zip": "20901"
}

# 2. Print formatted address (single print, multi-line)
print(f"""{contact_info["name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}""")

# 3. Remove name
contact_info.pop("name")

# 4. Create full_name dictionary
full_name = {
    "first name": "Hana",
    "last name": "Tilahun"
}

# 5. Add honorific
full_name.update({"honorific": "Ms."})

# 6. Add full_name to contact_info
contact_info.update({"full_name": full_name})

# 7. Print updated formatted address
print(f"""{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}""")
#Used a dictionary for contact info
#Used f-string with triple quotes for clean formatting
#Used .pop() to remove a key
#Used .update() to add new data
#Nested a dictionary inside another dictionary