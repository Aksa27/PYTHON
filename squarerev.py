nums=[]
count=0
while count <3:
    num=int(input("enter a number to reverse"))
    nums.append(num**2)
    count+=1
    
count=len(nums)-1
while 0<=count:
    print(nums[count],end="")
    count-=1