class student():
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("name",self.name)
        print("rollno",self.rollno)
    def setage(self,age):
        self.age=age
        print("age",self.age)
    def setmark(self,mark):
        self.mark=mark
        print("mark",self.mark)
student1=student("Akku",2267)
student1.setage(19)
student1.setmark(100)
student1.display()
        