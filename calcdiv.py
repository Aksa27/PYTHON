class calc:
    def __init__(self,n,m):
        self.num1=n
        self.num2=m
    def division(self):
        self.div=self.num1/self.num2
        return self.div
add1=calc(10,20)
print(add1.division())
add2=calc(20,15)
print(add2.division())