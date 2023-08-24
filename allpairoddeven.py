def even_odd(num):
    b=[]
    n=len(num)
    for i in range(n):
        for j in range(i+1,n):
            if(num[i]*num[j])%2==0 and (num[i]+num [j])%2==0:
                b.append((num[i],num[j]))
    return b
x=[2,3,4,5,6]
result_b=even_odd(x)
if result_b:
    print("pairs with even product and sum:")
    for b in result_b:
        print(b)            