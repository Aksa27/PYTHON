class calc:
    def __init__(self,n,m):
        self.num1=n
        self.num2=m
    def multiplication(self):
        self.mul=self.num1*self.num2
        return self.mul
add1=calc(10,20)
print(add1.multiplication())
add2=calc(20,15)
print(add2.multiplication())