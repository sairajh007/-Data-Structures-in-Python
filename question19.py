


#create a code to find union of list without duplicates 


list1=[1,2,3,4,5]
list2=[3,4,5,6,7]

union=[ ]

for i in list1:
    if i not in union:
        union.append(i)

for i in list2:
    if i not in union:
        union.append(i)


    
print(union)











