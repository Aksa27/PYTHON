list=[]
print("enter the integers")
while True:
    list1=input()
    if list1:
        list.append(list1)
    else:
        break
    c=max(list)
print(c)