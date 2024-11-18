

#create a code that prompts user to enter two sets of integers seperated by comma then print the intersection of these two sets


# Prompt the user for input and convert to sets of integers
set1 = set(map(int, input("Please enter set 1 (comma-separated): ").split(',')))
set2 = set(map(int, input("Please enter set 2 (comma-separated): ").split(',')))

# Find the intersection of the two sets
result_final = set1 & set2  # Use '&' for intersection of sets

# Print the result
print("Intersection of the two sets:", result_final)
