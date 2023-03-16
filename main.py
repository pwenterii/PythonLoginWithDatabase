import json

#Function for adding a new user to the .JSON file
def addNewUser():
  username = input("Choose your username: ")
  #For debuging purposes: print(username)

  #Other information
  first = 0
  second = 0

  #Compiles the data into a dictionary to add to the .JSON file
  newUser = {"username": f"{username}", "1st": first, "2nd": second}

  with open('data.json', 'r+') as file:
    #Loads the .JSON file
    fileData = json.load(file)
    #Adds the data to the
    fileData['users'].append(newUser)
    #Sets the position to the end
    file.seek(0)
    #Puts fildData at the end of the .JSON file
    json.dump(fileData, file, indent=4)

#Function accessing an old user from .JSON file
def findOldUser(user):
  with open('data.json', 'r+') as file:
    #Loads the data from the .JSON file
    fileData = json.load(file)
    #For debuging purposes: print(fileData)

    #Makes the data into a list to make it more accessable
    fileDataList = list(fileData.values())
    #For debuging purposes: print(fileDataList[0][0]["username"])

    #Runs through all of the usernames in the .JSON file
    for i in range(len(fileDataList[0])):
      if fileDataList[0][i]["username"] == user:
        #Grabs the information from the .JSON file under the username
        accountData = fileDataList[0][0]
        #For debuging purposes: print(accountData)
        #For debuging purposes: print(type(accountData))

  
def login():
  newOld = input("Do you have an account (y/n): ")

  match newOld:
    case "y":
      account = input("Please enter your username: ")
      findOldUser(account)
    case "n":
      addNewUser()
    case _:
      print("[ERROR]: Invalid Response")

login()