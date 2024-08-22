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


''' ==== MENU FUNCTIONS ==== '''

# Add

# Remove

# Search and Edit
