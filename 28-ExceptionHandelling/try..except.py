# Python Try Except
'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''
try:
	print(x)
except NameError:
	print("Varriable is not defined.")
except:
	print("Something else wemt worng!")

try:
	x = 5
	print(x)
except:	
	print("Something went wrong")
else:
	print("Nothing went wrong")

try:
	print(y)
except:	
	print("Something went wrong")
finally:
	print("The 'try except' is finished")

