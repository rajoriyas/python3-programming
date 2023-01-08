#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

'''
Note: Sets are unordered, so you cannot be sure in which order the items will appear.
'''

thisset = {'apple', 'mango', 'banana'}
print(thisset)

'''
Access Items
You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
'''

for x in thisset:
	print(x)

print("banana" in thisset)

'''Change Items
Once a set is created, you cannot change its items, but you can add new items.'''

#Add Items
thisset.add("orange")
print(thisset)

thisset.update([1, 2, 3])
print(thisset)

#Remove Item
thisset.remove("banana")
print(thisset)
'''
Note: If the item to remove does not exist, remove() will raise an error.
'''
thisset.discard('orange')
print(thisset)
'''
Note: If the item to remove does not exist, discard() will NOT raise an error.
'''

#pop()
x = thisset.pop()
print(thisset)
print(x)
'''
You can also use the pop(), method to remove an item, but this method will remove the last item. 
'''
thisset.clear()
print(thisset)

del thisset

myset = set(('rahul', 'rajoriya'))
print(myset)
