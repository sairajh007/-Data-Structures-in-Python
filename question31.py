


#Write a code that takes a list of words as input and returns a dictionary where the keys 
# are unique words
#and the values are the frequencies of those words in the input list&




# Take a list of words as input from the user
input_list = input("Enter a list of words (separated by spaces): ").split()

# Create an empty dictionary to store word frequencies
word_count = {}

# Iterate over the list of words and count their occurrences
for word in input_list:
    if word in word_count:
        word_count[word] += 1  # Increment the count if the word is already in the dictionary
    else:
        word_count[word] = 1  # Add the word to the dictionary with an initial count of 1

# Print the resulting dictionary
print("Word frequencies:", word_count)














