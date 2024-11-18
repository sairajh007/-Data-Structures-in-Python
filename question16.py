#create a code to check whether given list is sorted (either ascending or descending) or not





list=[1,2,42,50,43]


is_ascending=True
is_decending=True

for i in range(len(list)-1):
    if list[i]>list[i+1]:
        is_ascending=False
    if list[i<list[i+1]]:
        is_decending=False
    
if is_ascending:
    print("list is sorted in ascending order")
elif is_decending:
    print("list is sorted in descending order")
else:
    print("list is not sorted")












#easy way to sort list
# print(sorted(list))











