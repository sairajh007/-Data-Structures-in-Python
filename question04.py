


#Write a code to check if two given strings are anagrams of each other

'''
a="silent"
b="listen"

a=a.replace(" ","").lower()
b=b.replace(" ","").lower()

list1=list(a)
list2=list(b)

if len(list1)!=len(list2):
    print("strings are not anagrams")
else:
    for i in list1:
        for j in list2:
            if list1.count(i)!=list2.count(i):
                print("strings are not anagrams")
                break
            else:
                print("strings are angrams")

      
    
 ''' 


#easy way 
a = "silent"
b = "listen"

# Remove spaces and convert to lowercase
a = a.replace(" ", "").lower()
b = b.replace(" ", "").lower()

# Convert strings to lists of characters
list1 = sorted(list(a))
list2 = sorted(list(b))


#compare sorted list

if list1==list2:
    print("strings are anagrams")
else:
    print("strings are not anaragams")















