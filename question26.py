


#write a code that prompts uder to input two sets of characterb then print 
# union of these two sets 



# Prompt the user for input sets
set1 = set(input("Enter elements of the first set (comma-separated): ").split(','))
set2 = set(input("Enter elements of the second set (comma-separated): ").split(','))

# Compute the union of the two sets
result = set1 | set2  # Or use set1.union(set2)

# Print the result
print("Union of the two sets:", result)













