def common(words):
    b=[]
    for i in words:
        for j in words:
            if any(letter in j for letter in i):
                b.append((i,j))
    return b
x=['apple','banana','cherry','date'] 
b=common(x)
for b in b:
    print(b)           