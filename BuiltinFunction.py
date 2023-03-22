

# map Function
my_dict={
    'product_1' : 10,
    'product_2' : 1,
    'product_3' : 8,
}

def get_value(key):
    return my_dict[key]

key=['product_1','product_2','product_3']
output=list(map(get_value , key))
print(output)

# Filter Function Remove the values 

output=list(filter(get_value , key))
print(output)

# Lambda Function

x=2
y= lambda x : x*2
print(y(x))
