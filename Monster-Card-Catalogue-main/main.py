# This script manages the main player input: Add, Remove, Search/Edit, Quit
# This will be done in a while True loop. It breaks only when the user chooses to quit.

import easygui as eg
import catalogue_functions as functions

while True:
    user_input = eg.buttonbox(
        "What would you like to do?",
        choices=["Add", "Remove", "Search/Edit", "See Menu", "Quit"])
    if user_input == "Add":
        functions.add_monster()
    elif user_input == "Remove":
        functions.remove_monster()
    elif user_input == "Search/Edit":
        functions.search_and_edit_monster()
    elif user_input == "See Menu":
        formatted_catalogue = functions.format_catalogue()
        eg.msgbox(formatted_catalogue)
        print(formatted_catalogue)
    elif user_input == "Quit":
        eg.msgbox("Thank you for using the Monster Catalogue!")
        break