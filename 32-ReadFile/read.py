try:
	f = open("31-FileHandling/file.txt", 'rt')
	print(f.read())
except FileNotFoundError:
	print("File or Directory is not found.")
	f.close()
finally:	
	print("Program Completes!")
print("\n")

try:
	f = open("31-FileHandling/file.txt", 'rt')
	print(f.read(5))
	f.close()
except FileNotFoundError:
	print("File or Directory is not found.")
finally:	
	print("Program Completes!")
print("\n")

try:
	f = open("31-FileHandling/file.txt", 'rt')
	print(f.readline())
	print(f.readline())
	f.close()
except FileNotFoundError:
	print("File or Directory is not found.")
finally:	
	print("Program Completes!")
print("\n")

print("Line by Line")
print("\n")
try:
	f = open("31-FileHandling/file.txt", 'rt')
	for x in f:
		print(x)
	f.close()
except FileNotFoundError:
	print("File or Directory is not found.")
finally:	
	print("Program Completes!")
