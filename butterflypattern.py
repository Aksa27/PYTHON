def butterfly_pattern(n):
    for i  in range(n):
        for j in range(2*n):
            if j<=i or j>=2*n-i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    for i in range(n-2,-1,-1):
        for j in range (2*n):
            if j <=i or j>=2*n-i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
n=int(input("enter the size of the butterfly pattern:"))
butterfly_pattern(n)    
             
        