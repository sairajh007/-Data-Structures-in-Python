


#write a code to shuffle given list randomly without using any builtin shuffle function


import random

list=[1,2,3,4,5]

#using Fisher-Yates Shuffle (Knuth Shuffle) approach

for i in range(len(list)-1,0,-1):
    j=random.randint(0,i)
    list[i],list[j] = list[j],list[i]



print("shuffled listy",list)









