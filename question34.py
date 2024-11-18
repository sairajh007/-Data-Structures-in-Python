
# Write a code that takes a dictionary as input and returns a sorted version of it based on the values. You
#can choose whether to sort in ascending or descending order&



# Function to sort the dictionary based on values
def sort_dict_by_values(input_dict, descending=False):
    # Sort the dictionary by values using sorted() and a lambda function
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=descending))
    return sorted_dict

# Take dictionary input from the user
input_dict = eval(input("Enter a dictionary (e.g., {'apple': 3, 'banana': 2, 'orange': 5}): "))

# Ask the user if they want to sort in ascending or descending order
order = input("Do you want to sort in ascending order? (yes/no): ").lower()
descending = True if order == 'no' else False

# Get the sorted dictionary
sorted_dict = sort_dict_by_values(input_dict, descending)

# Print the sorted dictionary
print("Sorted dictionary:", sorted_dict)
















