fruit = ["Rahul", "Kusum", "Rajoriya"]
for x in fruit:
	print(x)

print('\n')
for x in "banana":
	print(x)

print('\n')
fruits = ("Rahul", "Kusum", "Rajoriya")
for x in fruits:
	print(x)
	if x == "Kusum":
		break

print('\n')
fruits = {"Rahul", "Kusum", "Rajoriya"}
for x in fruits:
	if x == "Kusum":
		break
	print(x)

print('\n')
name = {
	'first':"Rahul",
	'middle':'Kusum',
	'last':'Rajoriya'
}
for x, y in name.items():
	if x == 'middle':
		continue
	print(x, y)

print('\n')
for x in range(6):
	print(x)

print('\n')
for x in range(2, 6):
	print(x)

print('\n')
for x in range(2, 30, 3):
	print(x)

print('\n')
for x in range(6):
	print(x)
else:
	print("Finally Finished!")

print('\n')
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
	
