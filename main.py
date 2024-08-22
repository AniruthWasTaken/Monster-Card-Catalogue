# This script manages the main player input: Add, Remove, Search/Edit, Quit
# This will be done in a while True loop. It breaks only when the user chooses to quit.

import easygui as eg
import catalogue_functions as functions

while True:
  user_input = eg.buttonbox("What would you like to do?",
                            choices=["Add", "Remove", "Search/Edit", "Quit"])
  if user_input == "Add":
    functions.eg_non_empty_string("Une jetoj kuq e zi")
  elif user_input == "Remove":
    eg.msgbox("Cody")
  elif user_input == "Search/Edit":
    eg.msgbox("Luke")
  elif user_input == "Quit":
    eg.msgbox("Thank you for using the Monster Catalogue!")
    break
