# Python JSON

'''
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.
'''

import json
## some JSON:
x = '''{
	"name":"Rahul",
	"age":22
}'''

# parse x:
y = json.loads(x)

print(y)
print(y['age'])

# a Python object (dict):
x = {
	"name":"Rahul",
	"age":22
}

y = json.dumps(x)

print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
	'name':"rahul",
	'age':'30',
	'married':False,
	"children":("Me", "Myself"),
	'pets':None,
	"cars":[
		{"model": "BMW 230", "mpg": 27.5},
		{"model": "Ford Edge", "mpg": 24.1}	
	]
}

print(json.dumps(x))

# Format the Result
print(json.dumps(x, indent=2))
print(json.dumps(x, indent=5, separators=(",", "="))) #default value is (", ", ": ")

#Order the Result
print(json.dumps(x, indent=4, sort_keys=True))













