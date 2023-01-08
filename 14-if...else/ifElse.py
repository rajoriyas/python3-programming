a = 33
b = 203
if a>b:
	print(a)
else:
	print(b)

#Indentation
'''
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
'''
#Produce an error

#Elif
a = 33
b = 33
if a>b:
	print('Greater')
elif a==b:
	print('Equal')
else:
	print("Lesser")

#Short Hand If ... Else
print('A') if a>b else print('B')

print('A') if a>b else print('=') if a<b else print('B')
