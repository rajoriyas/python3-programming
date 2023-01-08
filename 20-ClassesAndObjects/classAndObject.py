# Python Classes/Objects
'''
Python is an object oriented programming language.
'''
# Create a Class
class MyClass:
	x=5

# Create Object
obj = MyClass()
print(obj.x)

# The __init__() Function
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

obj = Person("Rahul", 21)

print(obj.name)
print(obj.age)

# Object Methods
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def myfunc(self):
		print("Hello "+self.name)

obj = Person("Rahul", 22)
obj.myfunc()

# The self Parameter
class Person:
	def __init__(mysillyobject, name, age):
		mysillyobject.name = name
		mysillyobject.age = age
	def myfunc(abc):
		print("Hello "+abc.name+"\nAge "+str(abc.age))		
obj = Person("Rajoriya", 22)
obj.myfunc()

obj.age = 22
obj.myfunc()

del obj.age
# obj.myfunc()
 
del obj











