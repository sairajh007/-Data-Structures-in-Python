


#write a code to find intersection of two given list


list1=[1,2,3,4,5]
list2=[3,4,5,6,7]

intersection=[ ]


# Loop through each element in the first list
for element in list1:
    # Check if the element is in the second list and not already in the intersection
    if element in list2 and element not in intersection:
        intersection.append(element)


print(intersection)



