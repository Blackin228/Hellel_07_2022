class Person(object):

    def __init__(self, name, day_of_birthday, sex, day_of_death=None, surname=None, middle_name=None):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.day_of_birthday = day_of_birthday
        self.day_of_death = day_of_death
        self.sex = sex

    def __str__(self):
        return self.name + " " + self.surname + " " + self.middle_name + " " + self.day_of_birthday + \
               " " + self.day_of_death + " " + self.sex

    def create_list(self):
        return [self.name, self.surname, self.middle_name, self.day_of_birthday, self.day_of_death, self.sex]


# person = Person("Oleg", "21.04.2001", None, "male", "Sorochinskiy", "Viktorovich")
# print(person.create_list())
