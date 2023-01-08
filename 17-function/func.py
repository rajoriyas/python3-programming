def myfunc():
	print("Hello")

myfunc()

def myfunc(name):
	print("Hello "+name+"!")

myfunc('Rahul')

#Default Parameter Value
def myfunc(name = "World"):
	print("Hello "+name+"!")

myfunc('Rahul')
myfunc()

#Passing a List as a Parameter
def myfunc(name):
	print("Hello "+str(name)+"!")

name = ['Rahul', 'Kusum', 'Rajoriya']
myfunc(name)

def myfunc(x):
	return x**4

print(myfunc(3))

#Keyword Arguments
def myfunc(child3, child2, child1):
	print(child3)

myfunc('Rahul', 'Guddan', 'Varsha')
myfunc(child1='Rahul', child2='Guddan', child3='Varsha')

#Arbitrary Arguments
'''
If you do not now how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a "tuple" of arguments, and can access the items accordingly
'''

def myfunc(*child):
	for name in child:
		print(name)

myfunc("rahul", "kusum", 'rajoriya')

def fact(x):
	if x==1:
		return 1
	return(x*fact(x-1))

print(fact(7))
