

#write a code that take a tuple and a element as a input the function should return 
#the occurence of given elements in nthe tuple 



# Take tuple input from the user
input_tuple = tuple(map(int, input("Enter elements of the tuple (comma-separated): ").split(',')))

# Take element to check its occurrence
element = int(input("Enter the element to find its occurrence: "))

# Count the occurrence of the element in the tuple
occurrence = input_tuple.count(element)

# Print the result
print(f"The element {element} appears {occurrence} times in the tuple.")
















