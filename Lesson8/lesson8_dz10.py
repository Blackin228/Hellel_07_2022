values = [1, 2, '3', 'forth', 'end', 99, True, None]
print(f"Початковий список елементів: {values}")
output_list = list(map(lambda x: str(x) if type(x) == int else x, values))
print(f"Вихідний список елементів: {output_list}")
