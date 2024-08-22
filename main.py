# This script manages the main player input: Add, Remove, Search/Edit, Quit
# This will be done in a while True loop. It breaks only when the user chooses to quit.

import easygui as eg

while True:
  user_input = eg.buttonbox("What would you like to do?",
                            choices=["Add", "Remove", "Search/Edit", "Quit"])
  if user_input == "Add":
    eg.msgbox("Taylor")
  elif user_input == "Remove":
    eg.msgbox("Cody")
  elif user_input == "Search/Edit":
    eg.msgbox("Luke")
  elif user_input == "Quit":
    eg.msgbox("Thank you for using the Monster Catalogue!")
    break
