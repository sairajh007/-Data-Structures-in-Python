

#Write a code to access a value in a nested dictionary. The function should take the dictionary and a list of 
#keys as input, and return the corresponding value. If any of the keys do not exist in the dictionary, the
#function should return None


# Function to access a value in a nested dictionary
def access_nested_dict_value(nested_dict, keys_list):
    # Loop through the list of keys and access the nested dictionary
    for key in keys_list:
        # Check if the current key exists in the dictionary
        if key in nested_dict:
            nested_dict = nested_dict[key]  # Move to the next level of the nested dictionary
        else:
            return None  # Return None if the key does not exist
    return nested_dict  # Return the value when all keys are found

# Sample nested dictionary
nested_dict = {
    'a': {
        'b': {
            'c': 5,
            'd': 10
        },
        'e': 20
    },
    'f': 30
}

# List of keys to access
keys_list = ['a', 'b', 'c']

# Call the function and print the result
result = access_nested_dict_value(nested_dict, keys_list)
print(f"Result: {result}")














