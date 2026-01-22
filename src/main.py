import os
import sys
import sys
import json
import glob
from pathlib import Path

class ApplicationCore:
  @staticmethod
  def clear_screen(cls):
    # Check the operating system name and run the appropriate command
    if os.name == 'nt':
        _ = os.system('cls') # Windows
    else:
        _ = os.system('clear') # Linux/macOS/Posix

  def add_password(self, user_proflie, website, email, username, password):
   profile_json = f"password/proflie/{user_proflie}.json"
   if os.path.exists(profile_json):
    with open(profile_json, "r") as f:
     data = json.load(f)
    profile_name = data.get("profile_name")
    website = input("Enter -> Website Name ")
    email = input("Enter -> Email Used ")
    username = input("Enter -> Username ")
    password = input("Enter -> Password ")
   #profile_name = data.get("profile_name")
   new_data = {
             website: {
              "email": email,
              "username": username,
              "password": password,
            }
        }
   with open(profile_json, "w") as f:
    json.dump(new_data, f, indent="")
    print(f"Thanks, {username}! Your Account Details have been saved") 
    


  def remove_password(website, email, username, password):
   print("b")


  path = "password/proflie"
  contents = os.listdir(path)
  print("Directory contents:", contents)

  def login(self, user_proflie, password):
   os.makedirs("password/proflie", exist_ok=True) 
   print("---------------")
   user_proflie = input("Enter -> Proflie Name ")
   print("---------------")
   master_password = input("Enter -> Master Password ")
   profile_json = f"password/proflie/{user_proflie}.json"
   if os.path.exists(profile_json):
    with open(profile_json, "r") as f:
      data = json.load(f)
      username = data.get("username", "")
      if master_password == data.get("master"):
       profile_name = data.get("profile_name")
       self.clear_screen(cls="")
       print(f"Hello {profile_name} Welcome Back <𝟑 .ᐟ")
       print("--------- Choose Your Option ---------")
       print("1:) Add a Password? ")
       print("2:) Remove a Password? ")
       choice = input("Enter -> Choose Your Option: ") 
       if "1" in choice:
        self.add_password(user_proflie=user_proflie, website="", email="", username="", password="")
   else:
     print("g")
     profile_name = input("Enter -> The name you want us to call you ")
     while profile_name == "": #Simple check to make sure username is not empty because it just be weird 
      print("It seems that your username was empty please re-enter it!")
      profile_name = input("Enter -> The name you want us to call you ")
     username = input("Enter your username: ")
     while username == "": #Simple check to make sure username is not empty because it just be weird 
      print("It seems that your username was empty please re-enter it!")
      username = input("Enter your username: ")
     password = input("Enter your password: ")
     while password == "": #Simple check to make sure username is not empty because it just be weird 
      print("It seems that your password was empty please re-enter it!")
     password = input("Enter your password: ")
     file_name = input("Enter your file name for your password: ")
     while password == "": #Simple check to make sure username is not empty because it just be weird 
      print("It seems that your file name for your password was empty please re-enter it!")
      file_name = input("Enter your file name for your password: ")
     with open(profile_json, "w") as f: # Creates the username.json and ready to writes the username into it 
      json.dump({"profile_name": profile_name, "master": master_password, "username": username, "password": password, "file_name": file_name}, f, indent=4) # Dumps the username into the json file
     empty_data = {} 
     filename = f"{file_name}.json"
     with open(filename, 'w') as f_obj:
      json.dump(empty_data, f_obj)           
     print(f"Thanks, {username}! Your username has been saved")
     print(f"Created empty JSON file: {filename}")


  def save_user(proflie):
   profile_json = f"{username}.json"
   if os.path.exists(profile_json):
    with open(profile_json, "r") as f:
     data = json.load(f)
     username = data.get("username", "")

if __name__ == "__main__":
    app = ApplicationCore()
    app.login(user_proflie="", password="")