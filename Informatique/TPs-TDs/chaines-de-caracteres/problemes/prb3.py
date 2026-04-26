# =================================================================
# CPGE PYTHON CHALLENGE: STRING MANIPULATION (CH. 6.6)
# =================================================================

# -----------------------------------------------------------------
# CHALLENGE 1 (Moyen): The Data Sanitizer 🧹
# Goal: Use strip(), split(), slicing, capitalize(), and join()
# -----------------------------------------------------------------

raw_data = "  \n  item:mILK  ; item:bREAD  ; item:eGGS  \t  "

# TODO: 
# 1. Strip the whitespace and newlines from 'raw_data'.
# 2. Split the string by the ";" character to get a list.
# 3. For each item in that list:
#    - Remove the "item:" prefix (Hint: use slicing or .replace()).
#    - Clean any extra spaces left.
#    - Capitalize it properly (e.g., "mILK" -> "Milk").
# 4. Join the cleaned items with a " -> " separator.
raw_data=str.strip(raw_data).split(";")
raw_data=[n.split()[0].replace("item:","").capitalize() for n in raw_data]

print(raw_data)
final_data = " -> ".join(raw_data) # Your result here

print("--- CHALLENGE 1 ---")
print(f"Result: '{final_data}'")
# Expected: "Milk -> Bread -> Eggs"