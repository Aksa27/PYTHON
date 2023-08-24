class circle():
    def __init__(self,radius):
        self.radius=radius
    def get_Area(self):
        return 3.14*self.radius**2
    def get_circumference(self):
        return 2*3.14*self.radius
r=int(input("enter the radius:"))    
circle=circle(r)
print("area:",circle.get_Area())
print("circumference:",circle.get_circumference())
    