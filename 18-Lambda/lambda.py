x = lambda a : a+10
print(x(5))

x = lambda a, b, c : a**b*c
print(x(5,6,2))

def lambdafunc(n):
	return lambda a : a * n

mydoubler = lambdafunc(2)
print(mydoubler(6))

mytripler = lambdafunc(3)
print(mytripler(6))
