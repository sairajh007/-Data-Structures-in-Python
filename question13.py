


#Create a code to count the occurrences of each element in a list and return a dictionary with elements as
#keys and their counts as values


list=[1,2,3,4,5,6,1]

dic={ }

for i in list:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
    
print(dic)






