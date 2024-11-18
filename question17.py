# write a code to merge two sorted list into a single sorted list 


list=[1,4,2,5,7,6]
list2=[44,11,22,55,77,66]

i=0
j=0
final_list=[ ]


while i<len(list) & j<len(list2):
    if list[i]<list2[i]:
        final_list.append(list[i])
        j+=1
    else:
        final_list.append(list2[i])
        j+=1

while i < len(list):
    final_list.append(list[i])
    i += 1

# Add remaining elements from list2, if any
while j < len(list2):
    final_list.append(list2[j])
    j += 1

# Print the merged sorted list
print("Merged Sorted List:", final_list)
    











#easy way
'''
final_list=[ ]

final_list=sorted(list)+sorted(list2)

print(sorted(final_list))
'''











