try:
# "t" -> text mode, "b"-> binary mode
# "w" -> write mode, "r" -> read mode, "a" -> append mode, "x" -> creation mode
# "x" -> Create - will create a file, returns an error if the file exist
	f = open("write.txt", "wt") 
	f.write("Hello World!")
	f.close()
except:
	print("Error found!")
finally:
	print("Execution Complete.")

try:
	f = open("write.txt", "rt")
	for x in f:
		print(x)
	f.close()
except:
	print("Error found!")
finally:
	print("Execution Complete.")


try:
	f = open("write.txt", "at")
	f.write("This is append mode.")	
	f.close()
except:
	print("Error found!")
finally:
	print("Execution Complete.")


try:
	f = open("write.txt", "rt")
	for x in f:
		print(x)
	f.close()
except:
	print("Error found!")
finally:
	print("Execution Complete.")
