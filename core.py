from random import choice

def generatePassword():
	symbolsAmount = input("How many symbols?\n")
	smallLettersB = input("Should you use small letters? (Y/N)\n")
	bigLettersB = input("Should you use big letters? (Y/N)\n")
	digitsB = input("Should you use digits? (Y/N)\n")
	specialSymbolsB = input("Should you use special symbols? (Y/N)\n")
	availableCharacters = []
	password = ""
	
	if smallLettersB.upper() == "Y":
		availableCharacters += ["a", "b", "c",
								"d", "e", "f",
								"g", "h", "i",
								"j", "k", "l",
								"m", "n", "o",
								"p", "q", "r",
								"s", "t", "u",
								"v", "w", "x",
								"y", "z"] 
	if bigLettersB.upper() == "Y":
		availableCharacters += ["A", "B", "C",
								"D", "E", "F",
								"G", "H", "I",
								"J", "K", "L",
								"M", "N", "O",
								"P", "Q", "R",
								"S", "T", "U",
								"V", "W", "X", 
								"Y", "Z"]
	if digitsB.upper() == "Y":
		availableCharacters += ["1", "2", "3",
								"4", "5", "6",
								"7", "8", "9",
								"0"]
	if specialSymbolsB.upper() == "Y":
		availableCharacters += ["`", "!", "@",
								"\"", "#", "$",
								"%", "^", "&",
								"?", "*", "'",
								"+", "=", ".",
								",", "/", "\\",
								":", ";"]
		
	try:
		for i in range(int(symbolsAmount)):
			password += choice(availableCharacters)
	except (ValueError, IndexError):
		return "Failed to generate a password"
	
	if password == "":
		return "Failed to generate a password"
	else:
		return password

def setSite():
	site = input("Enter the site's URL: ")
	return site

def setLogin():
	login = input("Enter the login: ")
	return login

def setPassword():
	password = ""
	if input("Do you want to create password? (Y/N)\n").upper() == "Y":
		password = generatePassword()
	else:
		password = input("Enter the password: ")
	return password

def addOtherInformation():
	otherInformation:dict = {}
	while input("Do you want to add some information? (Y/N)\n").upper() == "Y":
		name = input("Enter the name: ")
		value = input("Enter the value: ")
		otherInformation[name] = value
	return otherInformation

def changeOtherInformation(dataDict):
	while True:
		print("Choose field:\n")
		for i in range(len(dataDict["OtherInformation"])):
			for informationKey, valueKey in dataDict["OtherInformation"].items():
				print(f"{i}. {informationKey}: {valueKey}\n")
		answer = input()
  
		try:
			dataDict["OtherInformation"][list(dataDict["OtherInformation"])[int(answer)]] = input("\nEnter the new value: ")
			return dataDict
		except (ValueError, IndexError):
			print("Enter the valid number")

def checkValidity(dataDict):
	while True:
		if input("Should you rewrite something? (Y/N)\n").upper() == "Y":
			number = input("Choose an paragraph: \n1. Site \n2. Login \n3. Password \n4. Another paragraph\n")
			if number == "1":
				dataDict["Site"] = setSite()
				break
			elif number == "2":
				dataDict["Login"] = setLogin()
				break
			elif number == "3":
				dataDict["Password"] = setPassword()
				break
			elif number == "4":
				dataDict = changeOtherInformation(dataDict)
				break
			else:
				print("Enter the valid number")
	return dataDict