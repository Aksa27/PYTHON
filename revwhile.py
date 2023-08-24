string=(input("enter a string"))
i=string
reverse='' 
while (len(i)>0):
    if (len(i)>0):
        a=i[-1]
        i=i[:-1]
        
    reverse += a
print(reverse) 