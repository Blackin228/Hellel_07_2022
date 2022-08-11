case = True
while case is True:
    name = input("Введіть ваше ім'я: ").title()
    age = input("Введіть ваш вік: ")
    if not age.isdigit() or int(age) <= 0:
        print("Помилка, повторіть введення")
    elif int(age) < 10:
        print(f"Привіт, шкет {name}")
    elif int(age) <= 18:
        print(f"Як життя {name}?")
    elif int(age) < 100:
        print(f"Що бажаєте {name}?")
    else:
        print(f"{name}, ви брешете - в наш час стільки не живуть...")
    choice = input("Хочете вийти? (Д/Y): ").lower()
    if choice == "y" or choice == "д":
        case = False
    print("-" * 50)
