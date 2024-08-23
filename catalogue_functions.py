# This script will act as a library for all the functions in this program
import easygui as eg
import catalogue_global_variables as data
''' ==== VALIDITY FUNCTIONS ==== '''


# Get integer with range check
def eg_integer_stat_range_check(prompt):
  '''Gets the user to input a whole number between the min stat value and the max stat value'''
  # Since the integer box already handles unexpected values and ranges
  # That is why I can just set the lower and upper bounds in the integer box function
  user_input = eg.integerbox(prompt,
                             lowerbound=data.min_stat_value,
                             upperbound=data.max_stat_value)
  # Return the end result (it will not return an invalid)
  return user_input


# Get string input return non empty
def eg_non_empty_string(prompt):
  '''Gets the user to input a string that is not empty'''
  user_input = ""  # Initialise the user input as an empty string
  while True:  # Eternal loop; only breaks when the user inputs something
    user_input = eg.enterbox(prompt)
    if user_input != "":
      break
    user_input = eg.msgbox("Please input something")
  return user_input


''' ==== HELPER FUNCTIONS ==== '''


# Get monster : stats from catalogue
def get_monster_and_stats():
  '''Gets the user to input a monster name, returns the monster stats'''
  user_input = eg_non_empty_string("Monster name:")
  while user_input not in data.catalogue:
    user_input = eg_non_empty_string(
        "That monster is not in the catalogue. Please try again.")
  temporary_monster = {}
  temporary_monster.update({user_input: data.catalogue[user_input]})
  return temporary_monster


def format_catalogue():
  '''Nicely formats the entire catalogue'''
  # The formatted catalogue is a string that contains the catalogue in a nice format
  formatted_catalogue = ""
  formatted_catalogue += "CATALOGUE \n\n"  # Add the title

  for monster in data.catalogue:
    formatted_catalogue += f"{monster}\n"

    formatted_catalogue += "- "
    for stat in data.catalogue[monster]:
      value = data.catalogue[monster][stat]
      formatted_catalogue += f"{stat}: {value}, "

    formatted_catalogue += "\n"

  return formatted_catalogue


def format_monster_card(monster_name):
  '''Nicely formats the monster card (must be in catalogue)'''

  if monster_name not in data.catalogue:
    eg.msgbox("That card is not in the catalogue")
    return

  formatted_monster_card = f"{monster_name}\n"
  for stat in data.catalogue[monster_name]:
    value = data.catalogue[monster_name][stat]
    formatted_monster_card += f"- {stat}: {value}\n"
  return formatted_monster_card


def get_monster_names():
  '''Returns all the monster'''
  monster_names_list = []
  for monster in data.catalogue:
    monster_names_list.append(monster)
  return monster_names_list


''' ==== MENU FUNCTIONS ==== '''


# Add
def add_monster():
  '''Get the user to add a monster to the catalogue'''
  # Temporary variables
  temporary_card = {}
  # Monster name
  monster_name = eg_non_empty_string("Monster name:")
  # Monster strength
  monster_strength = eg_integer_stat_range_check("Strength:")
  # Monster speed
  monster_speed = eg_integer_stat_range_check("Speed:")
  # Monster stealth
  monster_stealth = eg_integer_stat_range_check("Stealth:")
  # Monster cunning
  monster_cunning = eg_integer_stat_range_check("Cunning:")

  # Update the temporary card with the new details
  temporary_card.update({
      monster_name: {
          "Strength": monster_strength,
          "Speed": monster_speed,
          "Stealth": monster_stealth,
          "Cunning": monster_cunning
      }
  })

  formatted_string = f"{monster_name}\n- Strength: {monster_strength}\n- Speed: {monster_speed}\n- Stealth: {monster_stealth}\n- Cunning: {monster_cunning}\n"

  # Yes/No
  add_to_catalogue = eg.buttonbox(f"Details correct? \n\n{formatted_string}",
                                  choices=["Yes", "No"])
  # If Yes, add card to the catalogue
  if add_to_catalogue == "Yes":
    data.catalogue.update(temporary_card)


# Remove
def remove_monster():
  '''Get the user to remove a monster from the catalogue'''
  # Get the monster name with a choice box
  monster_to_remove = eg.choicebox("Which monster would you like to remove?",
                                   choices=get_monster_names())
  if monster_to_remove is None:
    return
  # Yes/No
  remove_from_catalogue = eg.buttonbox(
      "Are you sure you want to remove this monster?", choices=["Yes", "No"])
  if remove_from_catalogue == "Yes":
    data.catalogue.pop(str(monster_to_remove))


# Search and Edit
def search_and_edit_monster():
  '''Get the user to search and edit a monster in the catalogue'''
  monster_to_edit = eg.choicebox("Which monster card would you like to see?",
                                 choices=get_monster_names())
  edit_monster = eg.buttonbox(
      f"{format_monster_card(monster_to_edit)}\n\nDo you want to to edit this card?",
      choices=["Yes", "No"])
  if edit_monster == "No":
    return
  new_card = {}
  monster_name = eg_non_empty_string("Monster name:")
  # Monster strength
  monster_strength = eg_integer_stat_range_check("Strength:")
  # Monster speed
  monster_speed = eg_integer_stat_range_check("Speed:")
  # Monster stealth
  monster_stealth = eg_integer_stat_range_check("Stealth:")
  # Monster cunning
  monster_cunning = eg_integer_stat_range_check("Cunning:")

  apply_edits = eg.buttonbox("Apply edits?", choices=["Yes", "No"])
  if apply_edits == "No":
    return

  new_card.update({
      monster_name: {
          "Strength": monster_strength,
          "Speed": monster_speed,
          "Stealth": monster_stealth,
          "Cunning": monster_cunning
      }
  })
  data.catalogue.pop(str(monster_to_edit))
  data.catalogue.update(new_card)
