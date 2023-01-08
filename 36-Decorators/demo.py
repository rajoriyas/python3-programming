def parent(child):
	def inner():
		print("using decorator")
		child()
	return inner

def child1():
	print('child1')

child1=parent(child1)
child1()

@parent
def child2():
	print('child2')

child2()
