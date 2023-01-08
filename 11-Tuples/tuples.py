#thislist = ['apple', 'mango', 'banana']
thistuple = ("apple", "mango", "banana")
print(thistuple)

#Access Tuple Items
print(thistuple[1])
print('\n')

#Change Tuple Values
'''Once a tuple is created, you cannot change its values. Tuples are unchangeable.'''

#Loop Through a Tuple
for x in thistuple:
	print(x)

print('\n')
#Check if Item Exists
if "mango" not in thistuple:
	print("No")
else:
	print("Yes")

print(len(thistuple))

#Add Items
'''
Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
'''

#Remove Items
'''Note: You cannot remove items in a tuple.
'''

#The del keyword can delete the tuple completely
del thistuple

mytuple = tuple(('rahul', 'rajoriya'))
print(mytuple)

print(mytuple.index("rajoriya"))
