


#write a code to get two inputs set of integers then print their union,intersection
# and differences of these two sets

# Take two sets of integers as input from the user
set1 = set(map(int, input("Enter elements of the first set (comma-separated): ").split(',')))
set2 = set(map(int, input("Enter elements of the second set (comma-separated): ").split(',')))

# Union of the two sets (all unique elements from both sets)
union_result = set1 | set2

# Intersection of the two sets (common elements)
intersection_result = set1 & set2

# Difference of the two sets (elements in set1 but not in set2)
difference_result = set1 - set2

# Print the results
print("Union of the two sets:", union_result)
print("Intersection of the two sets:", intersection_result)
print("Difference of the two sets (set1 - set2):", difference_result)














