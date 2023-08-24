class bank:
    def __init__(self,name,accno,balance):
        self.name=name
        self.accountno=accno
        self.bal=balance
    def deposit(self):
        self.amt=int(input("enter amount:"))
        self.bal+=self.amt
        return self.bal
    def withdraw(self):
        self.amt=int(input("enter the amount"))
        self.bal-=self.amt
        return self.bal
    def balance(self):
        print("balance=",self.bal)
user1=bank("aksa",6688,34000)
print(user1.deposit())
print(user1.withdraw())
user2=bank("alby",6882,12500)
print(user2.deposit())
print(user2.withdraw())
user3=bank("akkusachu",9876,90876)     
print(user3.deposit())
print(user3.withdraw())
