a, b = map(int, input('Values:').split())
#x = lambda a,b: a>b
x = (a+b, a-b)[a>b]
print(x)
y = a<b and a-b or a+b
print(y)
