# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 5/4/2022
# Description: Takes a list of names, separates names that start with "K" and then adds a surname to each.
#

def add_surname(fore):
    """Takes a list of names, separates names that start with "K" and then adds a surname to each."""
    list = [name + 'Kardashian' for name in fore if name[0] == "K"]
    return list

#fore = ["Kiki", "Krystal", "Pavel", "Marykay", "Annie", "Koala"]
#surname = "Kardashian"
#print(add_surname())
#