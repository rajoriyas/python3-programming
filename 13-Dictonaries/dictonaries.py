#Dictionary
'''
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
'''
thisdict = {
	'brand':'ford',
	'model':'mustang',
	'year':1964
}
print(thisdict)
x = thisdict['year']
print(x)
y = thisdict.get('model')
print(y)

thisdict['year']=2019
print(thisdict)

#Key(index) and Item
for x in thisdict:
	print(str(x)+":"+str(thisdict.get(x)))

for x,y in thisdict.items():
	print(x, y)

#Check if Key Exists
if 'model' in thisdict:
	print(thisdict.get('model'))

print(len(thisdict))

#Adding Items
thisdict['color']='blue'
print(thisdict)

#Remove Key
thisdict.pop('year')
print(thisdict)

#Remove Item
'''
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
'''
thisdict.popitem()
print(thisdict)

#Remove Item by Key
del thisdict['model']
print(thisdict)

#Clear 
thisdict.clear()
print(thisdict)

#Delete Dict
del thisdict

#Copy
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

newdict = dict(thisdict)
print(newdict)

#Nested Dictionaries
myparent = {
	"child1":{
		'name':'rahul',
		'age':"21"	
	},
	'child2':{
		'name':'guddan',
		'age':"23"	
	},
	'child3':{
		'name':'varsha',	
		'age':"28"	
	}
}
print(myparent)

child1 = {
	'name':'rahul',
	'age':"21"	
}
child2 = {
	'name':'guddan',
	'age':"23"	
}
child3 = {
	'name':'varsha',	
	'age':"28"	
}
myparent = {
	"child1":child1,
	'child2':child2,
	'child3':child3	
}
print(myparent)

#The dict() Constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)

thisdict.insert("brand", "banz")
print(thisdict)














