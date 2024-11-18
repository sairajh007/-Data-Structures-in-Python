

#develop code that take input two sets of string and print the symmetric difference 
# of these two strings 


# Take two sets of strings as input from the user
set1 = set(input("Enter elements of the first set (comma-separated): ").split(','))
set2 = set(input("Enter elements of the second set (comma-separated): ").split(','))

# Calculate the symmetric difference between the two sets
symmetric_difference = set1 ^ set2  # Or you can use set1.symmetric_difference(set2)

# Print the result
print("Symmetric Difference of the two sets:", symmetric_difference)


















