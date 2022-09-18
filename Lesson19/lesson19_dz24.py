def generation_geometry_progression(value, den):
    while True:
        value *= den
        yield value


first_value = int(input("Введіть перший член прогресії: "))
denominator = int(input("введіть знаменник прогресії: "))

for item in generation_geometry_progression(first_value, denominator):
    if item > 1000:
        break
    print(item, end=", ")
