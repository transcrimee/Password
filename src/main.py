import os
import sys
import sys
import json


def login(user_proflie, password):
  print("---------------")
  user_proflie = input("Enter -> Proflie Name ")
  print("---------------")
  password = input("Enter -> Password ")
  profile_json = f"{user_proflie}.json"
  if os.path.exists(profile_json):
   with open(profile_json, "r") as f:
     data = json.load(f)
     username = data.get("username", "")
  else:
    print("g")
    username = input("Enter your username: ")
    while username == "": #Simple check to make sure username is not empty because it just be weird 
     print("It seems that your username was empty please re-enter it!")
     username = input("Enter your username: ")
    password = input("Enter your password: ")
    while password == "": #Simple check to make sure username is not empty because it just be weird 
     print("It seems that your password was empty please re-enter it!")
     password = input("Enter your password: ")
    with open(profile_json, "w") as f: # Creates the username.json and ready to writes the username into it 
     json.dump({"username": username, "password": password}, f, indent=4) # Dumps the username into the json file
    print(f"Thanks, {username}! Your username has been saved")


def save_user(proflie):
  profile_json = f"{username}.json"
  if os.path.exists(profile_json):
   with open(profile_json, "r") as f:
     data = json.load(f)
     username = data.get("username", "")

login(user_proflie="", password="")