# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead

cars = list(("rahul", "kusum", "rajoriya"))
print(cars[0])
cars[0] = 'rajoriyas'
print(cars[0])
print(len(cars))
for x in cars:
	print(x)
cars.append("rahul")
cars.pop(1)
cars.remove("rajoriyas")

print(cars)
