class Circle:
   def __init__(self,radius):#area of circle using oops concept
   	self.radius=radius
   def area(self):
   	return 3.14*self.radius**2
circle1=Circle(5)
print("Area:",circle1.area())
