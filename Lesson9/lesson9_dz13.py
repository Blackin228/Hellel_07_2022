print("""Ця програма вказує яке число ви ввели.
Якщо ви хочете вийти введіть значення з переліку ('exit, quit, q, e, вихід')""")

def check(message, item):
    if not item.replace(".", "").replace(",", "").replace("-", "").isdigit():
        message = "некоретне "
        return message, item
    if item[0] == "-":
        message += "від'ємне "
    else:
        message += "додатнє "

    if "," in item or "." in item:
        item = item.replace(",", ".")
        message += "дробове "
        if item.replace("-", "")[0] == ".":
            item = item.replace(".", "0.")
    else:
        message += "ціле "
    return message, item


while True:
    message = ""
    item = input("Ваше рішення:  ").lower()
    if item == "q" or item == "e" or item == "exit" or item == "quit" or item == "вихід":
        break
    else:
        answer = check(message, item)
        if "некоректне " in answer[0]:
            print(f"Ви ввели {answer[0]} число: {answer[1]}")
        else:
            print(f"Ви ввели {answer[0]} число: {answer[1]}")
    print("-" * 50)
