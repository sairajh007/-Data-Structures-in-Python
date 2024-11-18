

# Write a code to perform basic string compression using the counts of repeated characters


input_string = "aaabbbcc"

compressed_string = ""  # Initialize an empty string to store the result
count = 1  # Initialize count for the first character

for i in range(1, len(input_string)):
    if input_string[i] == input_string[i - 1]:
        count += 1
    else:
        compressed_string += input_string[i - 1] + str(count)
        count = 1  # Reset the count for the new character

compressed_string += input_string[-1] + str(count)

print("Compressed String:", compressed_string)
       



