


#write a code to take two input of tuple and returning new tuple containing element common in both tuple


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

# List to store common elements
common_elements = []

# Find common elements
for i in tuple1:
    if i in tuple2 and i not in common_elements:
        common_elements.append(i)

# Convert the list to a tuple
result_tuple = tuple(common_elements)

# Print the result
print(result_tuple)

















