# Python Inheritance

# Parent Class
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def info(self):
		print(self.name+" "+str(self.age))

obj1 = Person("Rahul", 22)
obj1.info()

# Child Class
class Student(Person):
	pass

'''
Note: Use the 'pass' keyword when you do not want to add any other properties or methods to the class.
'''

obj2 = Student("Rajoriyas", "21")
obj2.info()

class Employee(Person):
	def __init__(self, name, age):
		self.name = name
		self.age = age*12

obj3 = Employee("Kusum", 48)
obj3.info()

'''
Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
'''

class Parents(Person):
	def __init__(self, name, age):
		Person.__init__(self, name, age)


obj4 = Parents("Harish", 54)
obj4.info()

class GrandParents(Person):
	def __init__(self, name, age, year):
		super().__init__(name, age)
		self.graduationyear = year
	def info(self):
		super().info() # with super() no need to pass self
		print(self.graduationyear)

obj5 = GrandParents("Rampyari", 72, 2020)
obj5.info()
















