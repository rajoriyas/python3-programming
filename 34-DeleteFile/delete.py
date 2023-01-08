try:
	import os
	if os.path.exists("write.txt"):
		os.remove("write.txt")
		# Delete Folder
		os.rmdir("folder")
	else:
		print("file does not exists")
except:
	print("Error found!")
finally:
	print("Execution Complete.")

