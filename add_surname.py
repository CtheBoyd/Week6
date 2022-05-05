# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 5/4/2022
# Description: Takes a list of names, separates names that start with "K" and then adds a surname to each.
#



fore = ["Kiki", "Krystal", "Pavel", "Marykay", "Annie", "Koala"]
surname = "Kardashian"


def add_surname():
    #Takes a list of names, separates names that start with "K" and then adds a surname to each.
    k_fore = [i + " " + surname for i in fore if i[0] == "K"]
    return k_fore


print(add_surname())
