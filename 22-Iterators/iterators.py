mytuple = ('rahul', 'kusum', 'rajoriya')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "rajoriyas"
myit = iter(mystr)
i = 0
while i<len(mystr):
	print(next(myit))
	i += 1

print("\n")
#Looping Through an Iterator
for x in mytuple:
	print(x)

print("\n")
for x in mystr:
	print(x)

# Create an Iterator
class MyNum:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		x = self.a
		self.a += 1
		return x

obj1 = MyNum()
myiter = iter(obj1)

print("\n")
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) 

# StopIteration
class MyNum:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration

obj2 = MyNum()
myiter = iter(obj2)

print("\n")
for x in myiter:
	print(x)















