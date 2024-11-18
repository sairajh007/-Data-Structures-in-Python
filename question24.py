


#develop a code that prompt user to give two input sets of strings then print the element 
# that are present in first set and not in second set 

# Prompt the user to input two sets of strings (comma-separated)
set1 = set(input("Enter elements of the first set (comma-separated): ").split(','))
set2 = set(input("Enter elements of the second set (comma-separated): ").split(','))

# Find elements in set1 but not in set2
difference = set1 - set2

# Print the result
print("Elements present in the first set but not in the second set:", difference)



















