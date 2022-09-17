import openpyxl
from class_person import Person


def write_id_person():
    print("Ця функція має записувати інформацію про особу")
    name = input("Введіть ім'я: ")
    surname = input("Введіть прізвище: ")
    middle_name = input("Введіть по-батькові: ")
    day_of_birthday = input("Введіть дату народження: ")
    day_of_death = input("Введіть дату смерті: ")
    sex = input("Введіть стать: ")
    person = Person(name, day_of_birthday, sex, day_of_death, surname, middle_name)
    print(person)
    wb = openpyxl.Workbook()
    wb.create_sheet(title="First list", index=0)
    wb.remove(wb['Sheet'])
    sheet = wb["First list"]
    for col_index, column in enumerate(person.create_list()):
        for row_index, value in enumerate(column):
            cell = sheet.cell(row=row_index + 1, column=col_index + 1)
            cell.value = value
    wb.save('diplom.xlsx')


def search_id_person():
    print("Ця функція має здійснювати пошук за ознаками та виводити всі значення, які схожі")


while True:
    function = {"1": write_id_person, "2": search_id_person}
    print("""Дана програма дозволяє працювати з даними про людей
* Якщо ви хочете додати дані про людину натисніть 1
* Якщо ви хочете знайти дані про якусь людину натисніть 2
* Якщо ви хочете вийти натисніть 3""")
    selection = input("Введіть ваш вибір: ")
    if not selection.isdigit() or int(selection) == 0 or int(selection) > 3:
        print("Ви ввели некоректне значення, спробуйте ще")
        continue
    elif int(selection) == 3:
        break

    function[selection]()
