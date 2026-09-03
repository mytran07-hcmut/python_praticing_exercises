"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    #kiem tra equal
    if list_one == list_two:
        return EQUAL
        
    #kiem tra sublist
    if not list_one:
        return SUBLIST
    len_sub = len(list_one)
    for i in range(len(list_two) - len_sub + 1):
        if list_two[i:i + len_sub] == list_one:
            return SUBLIST

    #kiem tra superlist
    if not list_two:
        return SUPERLIST
    len_sub = len(list_two)
    for i in range(len(list_one) - len_sub + 1):
        if list_one[i:i + len_sub] == list_two:
            return SUPERLIST

    #kiem tra unequal
    else:
        return UNEQUAL