# Create a list (not in alphabetical order)
movies = ["Inception", "Avatar", "Titanic", "The Matrix"]

# --- 3. Print length and full list ---
print("The list movies includes my top " + str(len(movies)) + " favorite movies")
print(movies)

# --- 4a. Using sorted() ---
print(sorted(movies))   # temporary sorted version
print(movies)           # original list stays the same

# Observation:
# sorted() does NOT change the original list, it only returns a sorted copy

# --- 4b. Using .sort() ---
movies.sort()
print(movies)

# Observation:
# .sort() changes the original list permanently

# --- 5. Add a new movie ---
movies.append("Black Panther")

print("The list movies includes my top " + str(len(movies)) + " favorite movies")
print(movies)
#What you should notice:
#len() → counts items in the list
#sorted() → temporary sort (original list stays the same)
#.sort() → permanent change
#.append() → adds a new item to the list