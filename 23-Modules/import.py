import modules as mod
mod.greeting("Rahul")

print(mod.person['age'])

# Built-in Modules
import platform
x = platform.system()
print(x)

# Using the dir() Function
'''
There is a built-in function to list all the function names (or variable names) in a module. The dir() function

Note: The dir() function can be used on all modules, also the ones you create yourself.
'''
print(str(dir(platform)))
print('\n')
print(str(dir(mod)))

print('\n')
# Import From Module
from modules import person
print(str(person['age']))
