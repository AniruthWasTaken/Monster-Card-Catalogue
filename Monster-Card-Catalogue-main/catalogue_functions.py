# This script will act as a library for all the functions in this program
import easygui as eg
import catalogue_global_variables as data

''' ==== VALIDITY FUNCTIONS ==== '''


# Get integer with range check
def eg_integer_stat_range_check(prompt, title):
    """Gets the user to input a whole number between the min stat value and the max stat value"""
    # Since the integer box already handles unexpected values and ranges
    # That is why I can just set the lower and upper bounds in the integer box function
    user_input = eg.integerbox(msg=prompt, title=title, lowerbound=data.min_stat_value, upperbound=data.max_stat_value)
    # Return the end result (it will not return an invalid)
    return user_input


# Get string input return non-empty
def eg_non_empty_string(prompt, title):
    """Gets the user to input a string that is not empty"""
    user_input = ""  # Initialise the user input as an empty string
    while True:  # Eternal loop; only breaks when the user inputs a not empty string
        user_input = eg.enterbox(prompt, title=title)
        if user_input != "":
            break
        user_input = eg.msgbox("Please input something")
    return user_input


''' ==== HELPER FUNCTIONS ==== '''


# Get monster : stats from catalogue

def format_catalogue():
    """Nicely formats the entire catalogue"""
    # The formatted catalogue is a string that contains the catalogue in a nice format
    formatted_catalogue = ""
    formatted_catalogue += "CATALOGUE \n\n"  # Add the title

    # Add each monster card
    for monster in data.catalogue:
        # Add the monster name
        formatted_catalogue += f"{monster}\n"

        formatted_catalogue += "- "
        # Add each stat name and value
        for stat in data.catalogue[monster]:
            value = data.catalogue[monster][stat]
            formatted_catalogue += f"{stat}: {value}, "

        # Add new line for the next monster
        formatted_catalogue += "\n"

    return formatted_catalogue


def format_monster_card(monster_name):
    """Nicely formats the monster card (must be in catalogue)"""

    # Check if the monster name is not in the catalogue
    if monster_name not in data.catalogue:
        eg.msgbox("That card is not in the catalogue")
        return

    # Add the title
    formatted_monster_card = f"{monster_name}\n"
    # Add each stat and value to the string
    for stat in data.catalogue[monster_name]:
        value = data.catalogue[monster_name][stat]
        formatted_monster_card += f"- {stat}: {value}\n"
    return formatted_monster_card


def get_monster_names():
    """Returns all the monster names"""
    # Initialise the list
    # The list will contain the monster names
    monster_names_list = []
    # Add each monster name to the monster_names_list
    for monster in data.catalogue:
        monster_names_list.append(monster)
    return monster_names_list


def get_monster_names_lower_case():
    # Initialise a list
    # The list will contain all the monster names but lowercase
    monster_names_list = []
    # Add each lowercase monster name to the list
    for monster in data.catalogue:
        monster_names_list.append(monster.lower())
    return monster_names_list


''' ==== MENU FUNCTIONS ==== '''


# Add
def add_monster():
    """Get the user to add a monster to the catalogue"""
    while True:
        # Temporary variables
        temporary_card = {}
        # Monster name
        msg = "Monster name:"
        title = "Add monster"
        monster_name = eg_non_empty_string(msg, title)
        if monster_name is None:
            return
        while monster_name.lower() in get_monster_names_lower_case():
            msg = "A card with that name already exists! Please try again."
            monster_name = eg_non_empty_string(msg, title)
            if monster_name is None:
                return

        stats = {}
        for stat_name in data.stat_names:
            stat_value = eg_integer_stat_range_check(prompt=f"{stat_name}:", title=title)
            if stat_value is None:
                return
            stats.update({stat_name: stat_value})

        # Update the temporary card with the new details
        temporary_card.update({monster_name: stats})

        # Formatted catalogue
        formatted_string = f"{monster_name}\n"
        for stat in stats:
            formatted_string += f"- {stat}: {stats[stat]}\n"

        # Yes/No
        msg = f"Details correct? \n\n{formatted_string}"
        title = "Details correct?"
        add_to_catalogue = eg.buttonbox(msg=msg, title=title, choices=["Yes", "No"])
        # If Yes, add card to the catalogue
        if add_to_catalogue == "Yes":
            data.catalogue.update(temporary_card)
            print(format_monster_card(monster_name))
            break
        # If No, ask the user to re-enter the details
        else:
            msg = "Please re-enter the card details"
            title = "Card Details"
            eg.msgbox(msg=msg, title=title)


# Remove
def remove_monster():
    """Get the user to remove a monster from the catalogue"""
    if len(data.catalogue) == 1:
        msg = "There is one card remaining, you cannot remove it!"
        title = "Can't Remove"
        eg.msgbox(msg=msg, title=title)
        return
    while True:
        # Get the monster name with a choice box
        msg = "Which monster would you like to remove?"
        title = "Monster to Remove"
        monster_to_remove = eg.choicebox(msg=msg, title=title,choices=get_monster_names())
        if monster_to_remove is None:
            return
        # Yes/No
        msg = f"Are you sure you want to remove {monster_to_remove}?"
        title = "Remove?"
        remove_from_catalogue = eg.buttonbox(
            msg=msg,
            title=title,
            choices=["Yes", "No"])
        if remove_from_catalogue == "Yes":
            data.catalogue.pop(str(monster_to_remove))
            break


# Search and Edit
def search_and_edit_monster():
    """Get the user to search and edit a monster in the catalogue"""
    monster_to_edit = ""
    # If there is only one card left, make the choice box into a button box as the choice box does not like having less than 2 choices
    msg = "Which card would you like to edit?"
    title = "Card to Edit"
    if len(data.catalogue) > 1:
        monster_to_edit = eg.choicebox(msg=msg, title=title, choices=get_monster_names())
    else:
        monster_to_edit = eg.buttonbox(msg=msg, title=title, choices=get_monster_names())

    # If the user clicks the cancel button, the program goes back to the main menu
    if monster_to_edit is None:
        return
    # Initialise a new card dictionary
    new_card = {}
    monster_name = eg_non_empty_string("Monster name:", title)
    # If the user clicks the cancel button, the program goes back to the main menu
    if monster_name is None:
        return

    stats = {}
    # The user adds each stat value
    for stat_name in data.stat_names:
        stat_value = eg_integer_stat_range_check(f"{stat_name}:", title)
        # If the user clicks the cancel button, the program goes back to the main menu
        if stat_value is None:
            return
        stats.update({stat_name: stat_value})

    # Update the temporary card with the new details
    new_card.update({
        monster_name: stats
    })

    # Formatted catalogue
    formatted_string = f"{monster_name}\n"
    for stat in stats:
        formatted_string += f"- {stat}: {stats[stat]}\n"

    msg = f"Apply edits? \n\n{formatted_string}"
    title = "Apply Edits?"
    apply_edits = eg.buttonbox(msg=msg, title=title, choices=["Yes", "No"])
    if apply_edits == "No":
        return

    # Update the new card
    new_card.update({monster_name: stats})
    # Remove the old card from the catalogue
    data.catalogue.pop(str(monster_to_edit))
    # Add the new card to the catalogue
    data.catalogue.update(new_card)


def display_catalogue():
    print(format_catalogue())
    title = "Catalogue"
    eg.msgbox(msg=format_catalogue(), title=title)


def quit_catalogue():
    msg = "Thank you for using the Monster Catalogue!"
    title = "Bye"
    eg.msgbox(msg=msg, title=title)
