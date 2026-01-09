class cse:#Encapsulation
    def __init__(self):
   	self.pune="it is public"
   	self.__collector="it is private"
    def cat(self):
   	print(self.__collector)
obj=cse()
print(obj.pune)
obj.cat()
