
class Person:
    name = ""
    age = 0
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def get_age(self):
        return self.age

def std_dev(person_list):
    x = persons.get_age(self)
    sum_of_age = 0
    for i in age():
        sum_of_age + i
        avg = age / len(age)
        n = len(age)
        mean = sum(age) / n
        var = sum((i - avg) ** 2 for i in age()) / n
        std_dev = var ** 0.5
    return std_dev()

persons = Person
p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
person_list = [p1, p2, p3]
answer = std_dev(person_list)

print(answer)