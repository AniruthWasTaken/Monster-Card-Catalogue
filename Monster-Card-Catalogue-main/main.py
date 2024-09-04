# This script manages the main player input: Add, Remove, Search/Edit, Quit
# This will be done in a while True loop. It breaks only when the user chooses to quit.

import easygui as eg
import catalogue_functions as functions

while True:
    user_input = eg.buttonbox(
        "What would you like to do?",
        choices=["Add Card", "Remove Card", "Edit Card", "See Menu", "Quit"])
    if user_input == "Add Card":
        functions.add_monster()
    elif user_input == "Remove Card":
        functions.remove_monster()
    elif user_input == "Edit Card":
        functions.search_and_edit_monster()
    elif user_input == "See Menu":
        functions.display_catalogue()
    else:  # This can be the quit input or the x button in the top right
        functions.quit_catalogue()
        break
