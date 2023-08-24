def armstrong(n):
    rem,sum=0,0
    num=n
    while num>0:
        rem=num%10
        sum+= (rem**3)
        num//=10
        if sum==n:
            print(n,"is an armstrong:")
        else:
            print(n,"is not an armstrong")
x=int(input("enter a number:"))
armstrong(x)