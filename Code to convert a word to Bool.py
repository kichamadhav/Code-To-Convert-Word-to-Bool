#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
lst1 = list(string.ascii_lowercase)
lst2 = list(range(1,27))
dict1 = dict(zip(lst1,lst2))
lst3 = []
lst4 = []
lst5 = []
lst6 = []

a = 1

while a !=0:
    word = list(input("Enter the Word "))
    lst3 = word
    for i in range(len(lst3)):
        lst3[i]=lst3[i].lower()
    y = all(x in lst1 for x in lst3)
    
    if y != False:
        break
    elif y == False:
        print("Wrong Entry")
        continue
    
for k in lst3:
   
    if k in dict1:

            lst4.append(dict1.get(k))

for i in lst4: 
    if(i%2)==0:
        
        i = 0
        lst5.append(i)
    else:
        i = 1
        lst5.append(i)
        
for i in lst5: 
    if i == 0:
        
        i = False
        lst6.append(i)
    else:
        i = True
        lst6.append(i)
        
print(lst6)

