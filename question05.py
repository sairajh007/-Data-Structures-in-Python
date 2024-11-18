

# Write a code to find all occurrences of a given substring within another string


main_string = "hellohellohello"
sub_string = "hello"

# Initialize a list to store the starting positions of the substring
positions = []

# Loop through the main string
for i in range(len(main_string) - len(sub_string) + 1):
    # Check if the part of the string matches the substring
    if main_string[i:i + len(sub_string)] == sub_string:
        positions.append(i)  # Add the starting position to the list

# Print the positions of the substring
print("Positions of substring:", positions)





















