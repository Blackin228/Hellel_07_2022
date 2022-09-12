class Person(object):
    number_of_person = 0

    @staticmethod
    def print_about_class_person():
        print("This class is created to describe the characteristics of a person")

    @classmethod
    def total_persons(cls):
        print(f"Total persons: {cls.number_of_person}")

    @property
    def full_information(self):
        return self.name + ", " + self.surname + ", " + self.age + ", " + self.profession + ", " + self.sex

    @full_information.setter
    def full_information(self, new):
        self.name, self.surname, self.age, self.profession, self.sex = new.split(" ")

    def __init__(self, name=None, surname=None, age=None, profession=None, sex=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.profession = profession
        self.sex = sex
        Person.number_of_person += 1


person_1 = Person("Sirius", "Black", "43", "magician", "male")
person_2 = Person("Harry", "Potter", "20", "student", "male")
person_3 = Person()

print("Виклик статичного методу")
person_1.print_about_class_person()
person_2.print_about_class_person()
Person.print_about_class_person()
print("-" * 50)

print("Виклик методу класу")
person_1.total_persons()
person_2.total_persons()
Person.total_persons()
print("-" * 50)

print(person_1.full_information)
print(person_2.full_information)
person_1.surname = "White"
person_2.age = "26"
print(person_1.full_information)
print(person_2.full_information)
print("-" * 50)

person_3.full_information = "Bob Marley 36 musician male"
print(person_3.full_information)
print(person_3.name)
print(person_3.surname)
print(person_3.age)
print(person_3.profession)
print(person_3.sex)

