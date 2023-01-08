# RegEx
'''
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.
'''

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
x = re.findall("ai", txt)
print(x)
