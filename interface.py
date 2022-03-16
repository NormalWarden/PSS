import json
import hashlib
import core
from cryptography import getInitVectorAndKey, encryptWithInputData, decrypt


# Sign Up
def createDatabase():
	login = input("Enter login: ")
	password = input("Enter password: ")
	
	with open("userdata.json", 'r+') as outfile:
		data = json.load(outfile)

        # Default settings of JSON file
		data["login"] = hashlib.sha512(login.encode()).hexdigest()
		data["password"] = hashlib.sha512(password.encode()).hexdigest()
		data["content"] = []

		data["initvector"], data["key"] = getInitVectorAndKey()
  
        # Moving to start point of file and Saving Information
		outfile.seek(0)
		json.dump(data, outfile, indent=4)
		outfile.truncate()
		outfile.close()

# Sign In
def validUser():
	with open("userdata.json", 'r') as outfile:
		data = json.load(outfile)
  
		while True:
			print("")
			login = input("Enter the login: ")
			password = input("Enter the password: ")
			temp = 0
			if hashlib.sha512(login.encode()).hexdigest() == data["login"]:
				temp += 1
			if hashlib.sha512(password.encode()).hexdigest() == data["password"]:
				temp += 1
			if temp == 2:
				print("")
				break
			else:
				print("Data is invalid")
				temp = 0
		outfile.close()

# Entry = Place where contains data of accounts
def createEntry():
	with open("userdata.json", 'r+') as outfile:
		data = json.load(outfile)
		print("")
  
		site = core.setSite()
		login = core.setLogin()
		password = core.setPassword()
		otherInformation: dict = core.addOtherInformation()
		dataDict = {"Site": site,
					"Login": login,
					"Password": password,
					"OtherInformation": otherInformation}

		# Asking the user about validity of data
		print(f"Site: {dataDict['Site']}")
		print(f"Login: {dataDict['Login']}")
		print(f"Password: {dataDict['Password']}")
		for key, value in dataDict["OtherInformation"].items():
			print(f"{key}: {value}")
		dataDict = core.checkValidity(dataDict)

		# Encrypting all data
		dataDict["Site"] = encryptWithInputData(dataDict["Site"], data["initvector"], data['key'])
		dataDict["Login"] = encryptWithInputData(dataDict["Login"], data["initvector"], data['key'])
		dataDict["Password"] = encryptWithInputData(dataDict["Password"], data["initvector"], data['key'])
		for key, value in dataDict["OtherInformation"].items():
			dataDict["OtherInformation"][key] = encryptWithInputData(dataDict["OtherInformation"][key], data["initvector"], data['key'])
  
		data["content"].append([dataDict])
		outfile.seek(0)
		json.dump(data, outfile, indent=4)
		outfile.truncate()
		outfile.close()
	
def editEntry():
	with open("userdata.json", 'r+') as outfile:
		data = json.load(outfile)

		# Accounts count == 0
		if len(data["content"]) == 0:
			print("You have no one entry\n")
			return

		while True:
			print("Choose an entry:")
			for i in range(len(data["content"])):
				print(f"{i}. {decrypt(data['content'][i][0]['Site'], data['initvector'], data['key'])}")		
			answer = input()
			print("")

			# Exist 6 adoption stages
			# Denial
			# Anger
			# Bargaining
			# Depression
			# Adoption
			# And this part of code
			try:
				# Printing data of account
				index = 0
				for key, value in data["content"][int(answer)][0].items():
					if isinstance(value, dict):
						if bool(value): # If dict is not empty
							if index == 3:
								print("3. Another information\n")
							else:
								print(f"{index}. {list(value.items())[0][0]}: {decrypt(list(value.items())[0][1], data['initvector'], data['key'])}")
					else:
						print(f"{index}. {key}: {decrypt(value, data['initvector'], data['key'])}")
					index += 1
				answer1 = input()
				print("")

				# User choose OtherInformation
				if answer1 == "3":
					if len(data["content"][int(answer)][0]['OtherInformation']) == 0:
						print("You have no other inforamtion")
					else:
						print("Choose a field:\n")
						for h in range(len(data["content"][int(answer)][0]['OtherInformation'])):
							print(f"{h}. {list(data['content'][int(answer)][0]['OtherInformation'].items())[h][0]}: {decrypt(list(data['content'][int(answer)][0]['OtherInformation'].items())[h][1], data['initvector'], data['key'])}")
						answer2 = input()
						value = input("Enter the value: ")
						data["content"][int(answer)][0]["OtherInformation"][list(data["content"][int(answer)][0]["OtherInformation"].items())[int(answer2)][0]] = encryptWithInputData(value, data["initvector"], data['key'])
				# User choose Password or Something else
				else:
					if answer1 == "2":
						value = core.setPassword()
					else:
						value = input("Enter the value: ")
					data["content"][int(answer)][0][list(data['content'][int(answer)][0].items())[int(answer1)][0]] = encryptWithInputData(value, data["initvector"], data['key'])
				
				outfile.seek(0)
				json.dump(data, outfile, indent=4)
				outfile.truncate()
				print("Change is saved")
				break
			except (ValueError, IndexError):
				print("Enter the valid data\n")
		outfile.close()

# Printing data of account
def checkEntry():
	with open("userdata.json", 'r') as outfile:
		data = json.load(outfile)
  
		if len(data["content"]) == 0:
			print("You have no one entry\n")
			return
		else:
			while True:
				print("Choose an entry:\n")
				for i in range(len(data["content"])):
					print(f"{i}. {decrypt(data['content'][i][0]['Site'], data['initvector'], data['key'])}")
				answer = input()
				
				try:
					for key, value in data["content"][int(answer)][0].items():
						if isinstance(value, dict):
							if bool(value):
								for j in list(value.items()):
									print(f"{list(value.items())[0][0]}: {decrypt(j[1], data['initvector'], data['key'])}")
						else:
							print(f"{key}: {decrypt(value, data['initvector'], data['key'])}")
					print("")
					break
				except (ValueError, IndexError):
					print("Enter the valid number\n")
     
		outfile.close()