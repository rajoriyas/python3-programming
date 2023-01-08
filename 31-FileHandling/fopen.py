try:
	f = open("31-FileHandling/file.txt", 'rt')
except FileNotFoundError:
	print("File or Directory is not found.")
finally:	
	print("Program Completes!")
