class Animal:#Inheritance
  def speak1(self):
	print("I am an animal")
class dog(Animal):
  def speak2(self):
	print("I bark")
dog1=dog()
dog1.speak1()
dog1.speak2()
