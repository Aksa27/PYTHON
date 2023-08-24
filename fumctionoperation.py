def sum():
    n=int(input("enter the first number "))
    m=int(input("enter the second number"))
    print(n+m)
def sub():
    n=int(input("enter the first number"))    
    m=int(input("enter the second number"))
    print(n-m)
while True:
    ch=int(input("enter the choice:"))
    if ch==1:
        sum()
    elif ch==2:
       sub()
    elif ch==3:
        print("invalid choice")
        break
