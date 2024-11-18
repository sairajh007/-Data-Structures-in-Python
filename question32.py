


#Write a code that takes two dictionaries as input and merges them into a single dictionary. If there are
#common keys, the values should be added together&



# Take two dictionaries as input from the user
dict1 = eval(input("Enter the first dictionary: "))
dict2 = eval(input("Enter the second dictionary: "))

# Merge the two dictionaries
merged_dict = dict1.copy()  # Create a copy of the first dictionary to avoid modifying the original

for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value  # Add the values if the key exists in both dictionaries
    else:
        merged_dict[key] = value  # Otherwise, add the new key-value pair

# Print the resulting merged dictionary
print("Merged Dictionary:", merged_dict)














