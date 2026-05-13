# Original data
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# --- 3. Convert to lowercase ---
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# --- 4. Convert to title case ---
print(name_1.title())
print(name_2.title())
print(name_3.title())

# --- 5. Remove $ using replace() ---
salary_1_clean = salary_1.replace("$", "")
salary_2_clean = salary_2.replace("$", "")

print(salary_1_clean)
print(salary_2_clean)

# Check type
print(type(salary_1_clean))
print(type(salary_2_clean))

# Observation:
# They are still strings, so we need to remove commas and convert to int to do math

# --- 6. Chain replace() and int() ---
salary_1_int = int(salary_1.replace("$", "").replace(",", ""))

print(salary_1_int)
print(type(salary_1_int))