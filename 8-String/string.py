print('Hello')

a = 'rahul'
print(a)

# Multiline String
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = 'Hello World!'
print(a[2])

# Slicing
print(a[2:5])

# Negative Index Slicing
print(a[-5:-1])

# String Length
a = 'Hello World'
print(len(a))

# Remove the white spaces from begining and end
a = ' Hello World! '
print(a.strip())

#Lowercase
print(a.lower())

#Uppercase
print(a.upper())

#Replace
print(a.replace('H', 'J'))

#Split
print(a.split())
print(a.split(","))

#Search 
txt = "The rain in Spain stays mainly in the plain"
x = 'ain' in txt
print(x)

#Search 
txt = "The rain in Spain stays mainly in the plain"
x = 'ain' not in txt
print(x)

#Concatenation
a = "Hello "
b = "World"
print(a+b)

#String format 
age = 36
txt = "My name is John, I am " + str(age)
print(txt)

a = 3
b = 'rahul'
c = 66.8
txt = "{} person of same name {} have same weight {}"
print(txt.format(a,b,c))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

