# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 5/4/2022
# Description: Takes list of names and ages, returns the population standard deviation.
#

class Person:
    """Takes list of names and ages and splits the list into names list and ages list."""
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_age(self):
        return self.age


def std_dev(person_list):
    """Gets population standard deviation from ages list."""
    sum_age = 0
    n = len(person_list)
    for i in range(0, len(person_list)):
        sum_age += person_list[i].get_age()
    mean_age = sum_age / n
    squared_sum = 0
    for i in range(0, len(person_list)):
        numerator = squared_sum + (person_list[i].get_age()-mean_age)**2
    std = ((numerator / n) ** 2) * 0.5
    return std

#p1 = Person("Kyoungmin", 73)
#p2 = Person("Mercedes", 24)
#p3 = Person("Beatrice", 48)
#person_list = [p1, p2, p3]
#answer = std_dev(person_list)
#
#print(answer)
#