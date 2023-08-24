x=[""]
count={}
index=0
length=len(x)
while index<length:
    chr=x[index]
    count[chr]+=1
else:
    count[chr]=1
    index +=1    
print(len(x))
