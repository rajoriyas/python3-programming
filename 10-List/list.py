thislist = ['apple', 'banana', 'cherry']
print(thislist)

print(thislist[0]+'\n')

#Negative Indexing

#Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc
print(thislist[-1])
print(thislist[-2])
print(thislist[-3])

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Range of Negative Indexes
#This example returns the items from index -4 (included) to index -1 ("excluded")
print(thislist[-4:-1])

thislist[1] = 'blackcurrant'
print(thislist)
print("\n")

#Loop Through a List
for x in thislist:
	print(x)

#Check if Item Exists
if "blackcurrant" in thislist:
	print("\nyes")

#List Length
print(len(thislist))

#Add Items
thislist.append("grappes")
print(thislist)

thislist.insert(1, 'banana')
print(thislist)

#Remove Item
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index, (or the "last item" if index is not specified):
thislist.pop()
print(thislist)

thislist.pop(4)
print(thislist)

#The clear() method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#The del keyword can also delete the list completely:
del thislist

#Copy a List
#You cannot copy a list simply by typing list2 = list1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#The list() Constructor
#It is also possible to use the list() constructor to make a new list.
newlist = list(('rahul', 'rajoriya'))
print(newlist)

#Index of Item in list
print(newlist.index('rahul'))
