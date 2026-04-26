# --- CHALLENGE ---
# 1. Clean each name: Remove the extra spaces and fix the capitalization.
# 2. Join them: Create a single string where names are separated by a comma and a space.

names = ["  albert  ", "bEttY", "  CHArles  "]

# TODO: Your code goes here
# Hint: You need to transform each item in the list before using .join()
for i in range(len(names)):
    names[i]=names[i].split()[0].capitalize()
# Simple One:
# This creates a new list by applying strip and capitalize to every 'n' in names
# clean_names = [n.strip().capitalize() for n in names]
# final_string = ", ".join(clean_names)

final_string = str.join(", ", names)

print(final_string)

print(f"Result: '{final_string}'")
# Expected Output: "Albert, Betty, Charles"