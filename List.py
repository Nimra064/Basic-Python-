# Display the List Iterm 

L=[1,'2','a', True]

for i in L:
    print(i)


# Display the List with address

L=[1,'2','a', True]
iterm=(0,'a')
key , value= iterm
for key , value in enumerate(L):
    print(key , value)