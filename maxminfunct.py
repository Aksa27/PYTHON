def max_min(list):
    max_val=list[0]
    min_val=list[0]
    
    for num in list:
        if num>max_val:
         max_val=num
        if num<min_val:
            min_val=num
    return max_val,min_val
my_list=[1,34,5,10,12]
max_value,min_value=max_min(my_list)
print("maximum value:",max_value)
print("minimum value:",min_value)