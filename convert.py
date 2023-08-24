class convert():
    def __init__(self):
       self.num={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VII',9:'IX',10:'X'}
    def int_roman(self,num):
        if num<1 or num>10:
            raise ValueError("number out of range id (1-10)")
        return self.num(num)
convert1=convert()
number=int(input("enter the number:"))
roman=convert1.roman(number)
print(f"{number} in roman number is :{roman}")    
        
        
            
                