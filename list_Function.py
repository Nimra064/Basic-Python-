

# List Function :
input_user_list=[1,3,'5',True,'hello']
# Insert 
input_user_list.insert(1,'world')
# Remove
input_user_list.remove('5')
print(input_user_list)
# Append
input_user_list.append(0)
# extend
input_user_list.extend([1,7,9])
# Count
x=input_user_list.count(0)
print('Count the 0 element in the List =' , x)
# Lenght
len=len(input_user_list)
print('Lenght of the Element in the List =' , len)
# pop
input_user_list.pop(3)
print(input_user_list)

# sort list
New_List=[9,4,6,8,1,3,60]
New_List.sort(reverse=True)
print(New_List)

# sorted(New_List , reverse=True)
# print(New_List)

# String
input_string='I Love Pakistan'
input_string=input_string.upper()
print('Upper Case of Letter',input_string)

input_string=input_string.lower()
print('Lower Case of Letter ',input_string)

input_string=input_string.title()
print('Title of Text', input_string)



