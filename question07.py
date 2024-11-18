

# Write a code to determine if a string has all unique characters


input_string="abcd"

seen=set( )


for char in input_string:
    if char in seen:
        print("string not have unique characters")
    else:
        seen.add(char)

print("string have unique character",seen)





















