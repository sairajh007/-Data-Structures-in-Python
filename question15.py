


#Implement a code to find and remove duplicates from a list while preserving the original order of
#elements


list=[1,2,3,4,5,2]
u_list=[ ]



for i in list:
    is_duplicate=False

    for j in u_list:
        if i==j:
            is_duplicate=True

            break

    if not is_duplicate:
        u_list.append(i)

print("original list", list)
print("list after removing duplicates",u_list)








#easy way
print(dict.fromkeys(list))

