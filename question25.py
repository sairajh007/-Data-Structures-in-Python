

#create a code that take a tuple and two integers as input. 
# the function should return a new tuple containing element from original 
# tuple within the specified range of indices


# Take tuple input from the user
input_tuple = tuple(map(int, input("Enter elements of the tuple (comma-separated): ").split(',')))

# Take two integers as input for the range of indices
start_index = int(input("Enter the starting index: "))
end_index = int(input("Enter the ending index: "))

# Slice the tuple using the specified range of indices
sliced_tuple = input_tuple[start_index:end_index]

# Print the resulting tuple
print("New tuple within the specified range:", sliced_tuple)



















