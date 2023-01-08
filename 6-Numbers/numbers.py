x = 1    # int
y = 2.8  # float
z = 1j   # complex #z = -87.7e100
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

#Type Conversion

a = float(x)
b = int(y)

c = complex(x)
d = complex(y)
print(type(a))
print(type(b))

print(a)
print(b)

print(type(c))
print(type(d))

print(c)
print(d)

#You cannot convert complex numbers into another number type.

import random

print(random.randrange(1,10))
