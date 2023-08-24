class student():
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("name",self.name)
        print("rollno",self.rollno)
        print("age",self.age)
        print("mark",self.mark)
    def setage(self,age):
        self.age=age
    def setmark(self,mark):
        self.mark=mark
name=input("enter the name:")
rollno=int(input("enter the rollno:"))
student1=student(name,rollno)
age=int(input("enter the age:"))
marks=float(input("enter the marks:"))
student1.setage(age)
student1.setmark(marks)
student1.display()
        
    
        