# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 5/4/2022
# Description: Takes list of names and ages, returns the population standard deviation.
#




import math

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

        def get_age(self):
            return self.age

def show_person(person_list):
    """doc string 2"""
    for person in person_list:
      print("Name:", person.name, "\t Age:", person.age)

def std_dev(person_list):
  """doc string 3"""
  total, mean, sd = 0.0, 0.0, 0.0
  # No reason to take length of list as argument
  # We can just get it this way
  length = len(person_list)
  for person in person_list:
    total += person.age

  mean = total / length

  for person in person_list:
    sd += math.pow(person.age - mean, 2)
  return math.sqrt(sd / length)

p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
person_list = [p1, p2, p3]
answer = std_dev(person_list)

print(answer)