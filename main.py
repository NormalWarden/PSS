import interface

if __name__ == "__main__":
	while True:
		answer = input("Create database or edit?\n1. Create database\n2. Edit database\n")
		if answer == "1":
			interface.createDatabase()
			break
		elif answer == "2":
			interface.validUser()
			break
		else:
			print("Enter 1 or 2\n")
  
	while True:
		answer = input("What do you want to do?\n1. Create Entry\n2. Edit Entry\n3. Check the Entry\n")
		print("")
		if answer == "1":
			interface.createEntry()
		elif answer == "2":
			interface.editEntry()
		elif answer == "3":
			interface.checkEntry()
		else:
			print("Enter the valid number\n")