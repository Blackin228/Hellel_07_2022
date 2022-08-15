
old_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
new_dict = {value: key for key, value in old_dict.items()}
print("Початковий словник: ", old_dict)
print("Новий словник: ", new_dict)
