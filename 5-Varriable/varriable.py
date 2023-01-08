x = 5
y = "Rahul"
print(x)
print(y)

x = 'Rajoriya'
print(x)

x = 4
y = 6
print(x+y)

x = 'awasome'
def myfunc():
	x = 'fantastic'
	print(x)
myfunc()
print(x)

def myfunc():
	global x 
	x = 'fantastic'
	print(x)
myfunc()
print(x)
