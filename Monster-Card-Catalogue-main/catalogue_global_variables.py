# This script contains the catalogue dictionary and the min-max stat values
"""
Minimum stat value = 1
Maximum stat value = 25

Dictionary will be nested: {monster_name : {stat_name : stat_value}}

Entry example:
"Stoning":
{
  "Strength" : 7,
  "Speed" : 1,
  "Stealth" : 25,
  "Cunning" : 15
}

"""

min_stat_value = 1
max_stat_value = 25

so_once_upon_a_time_there_was_a_logitech_mouse_jawline = True

catalogue = dict(Stoneling={
    "Strength": 7,
    "Speed": 1,
    "Stealth": 25,
    "Cunning": 15
}, Vexscream={
    "Strength": 1,
    "Speed": 6,
    "Stealth": 21,
    "Cunning": 19
}, Dawnmirage={
    "Strength": 5,
    "Speed": 15,
    "Stealth": 18,
    "Cunning": 22
}, Blazegolem={
    "Strength": 15,
    "Speed": 20,
    "Stealth": 23,
    "Cunning": 6
}, Websnake={
    "Strength": 7,
    "Speed": 15,
    "Stealth": 10,
    "Cunning": 5
}, Moldvine={
    "Strength": 21,
    "Speed": 18,
    "Stealth": 14,
    "Cunning": 5
}, Vortexwing={
    "Strength": 19,
    "Speed": 13,
    "Stealth": 19,
    "Cunning": 2
}, Rotthing={
    "Strength": 16,
    "Speed": 7,
    "Stealth": 4,
    "Cunning": 12
}, Froststep={
    "Strength": 14,
    "Speed": 14,
    "Stealth": 17,
    "Cunning": 4
}, Wispghoul={
    "Strength": 17,
    "Speed": 19,
    "Stealth": 3,
    "Cunning": 2
})
