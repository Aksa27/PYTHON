l=['apple','mango']
k,a=" "
l2=[]
def vow():
    for i in range(0,len(l)):
        a=l[i]
        for j in range (0,len(a)):
            if a[j] not in "aieou":
                k+=a[j]
        l2.append(k)
        l(l2)
        vow()