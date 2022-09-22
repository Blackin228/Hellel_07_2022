import datetime


class Person(object):

    def __init__(self, name, day_of_birthday, sex, day_of_death=None, surname=None, middle_name=None):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.day_of_birthday = Person.create_date(day_of_birthday)
        if day_of_death == "":
            self.day_of_death = None
        else:
            self.day_of_death = Person.create_date(day_of_death)
        self.sex = sex
        self.age = Person.age_calculation(self)

    @staticmethod
    def create_date(date):
        change_date = date.replace(",", ".").replace("-", ".").replace("/", ".").replace(" ", ".").split(".")
        return datetime.date(int(change_date[2]), int(change_date[1]), int(change_date[0]))

    def age_calculation(self):
        if self.day_of_death is None:
            age = (datetime.date.today() - self.day_of_birthday).days // 365
            return age
        else:
            age = (self.day_of_death - self.day_of_birthday).days // 365
            return age

    def create_list(self):
        return [self.name, self.surname, self.middle_name, self.day_of_birthday, self.day_of_death, self.sex, self.age]

    @staticmethod
    def print_list(list_xlsx):
        output = list_xlsx[0] + " " + list_xlsx[1] + " " + list_xlsx[2] + " " + list_xlsx[6] + " " + "роки,"
        if "ч" in list_xlsx[5]:
            output = output + "чоловік. Народився: " + list_xlsx[3].replace("00:00:00", "")
        elif "ж" in list_xlsx[5]:
            output = output + "жінка. Народилась: " + list_xlsx[3].replace("00:00:00", "")
        if not list_xlsx[4] != None and "ч" in list_xlsx[5]:
            output = output + " Помер: " + list_xlsx[4].replace("00:00:00", "")
        elif not list_xlsx[4] != None and "ж" in list_xlsx[5]:
            output = output + " Померла: " + list_xlsx[4].replace("00:00:00", "")
        return output


