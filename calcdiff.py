class calc:
    def __init__(self,n,m):
        self.num1=n
        self.num2=m
    def substraction(self):
        self.diff=self.num1-self.num2
        return self.diff
add1=calc(10,20)
print(add1.substraction())
add2=calc(20,15)
print(add2.substraction())

