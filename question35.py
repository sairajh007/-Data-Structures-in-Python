

#Write a code that inverts a dictionary, swapping keys and values. Ensure that the inverted dictionary
#correctly handles cases where multiple keys have the same value by storing the keys as a list in the
#inverted dictionary.



# Function to invert the dictionary
def invert_dict(input_dict):
    inverted_dict = {}

    # Iterate over the original dictionary
    for key, value in input_dict.items():
        # If the value is already a key in the inverted dictionary, append the key to the list
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]  # Create a new list with the current key

    return inverted_dict

# Take a dictionary input from the user
input_dict = eval(input("Enter a dictionary (e.g., {'a': 1, 'b': 2, 'c': 1}): "))

# Get the inverted dictionary
inverted_dict = invert_dict(input_dict)

# Print the inverted dictionary
print("Inverted dictionary:", inverted_dict)











