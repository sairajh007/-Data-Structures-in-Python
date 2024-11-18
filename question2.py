

#Write a code to count the number of vowels in a string
'''
string="sairaj"
count=0

for i in string:
    if (i=="a") | (i=="A"):
        count+=1
    elif (i=="e") | (i=="E"):
        count+=1
    elif (i=="i") | (i=="I"):
        count+=1
    elif (i=="o") | (i=="O"):
        count+=1
    elif (i=="u") | (i=="U"):
        count+=1
    else:
        print("no vowels")

print(count)
'''


#easy method
string = "sairaj"
count = 0

# Define the set of vowels
vowels = "aeiouAEIOU"

# Loop through the string and check membership in vowels
for i in string:
    if i in vowels:
        count += 1

print(count)




