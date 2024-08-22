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
  user_input = ""  # Initialise the user input as an empty string
  while True:  # Eternal loop; only breaks when the user inputs something
    user_input = eg.enterbox(prompt)
    if user_input != "":
      break
    user_input = eg.msgbox("Please input something")
  return user_input


# Get monster : stats from catalogue
''' ==== MENU FUNCTIONS ==== '''

# Add

# Remove

# Search and Edit
