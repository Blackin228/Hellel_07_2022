# варіант для циклу while:
print("WHILE")
start = 0
output = 0
num = int(input("Введіть будь-яке число: "))
while start < num:
    start += 1
    if start % 3 == 0:
        print(f"Число {start} кратне 3, тому воно пропускається.")
        continue
    output += start ** 3
    print(f"Число, яке має підноситися до степеня: {start}")
    print(f"Сума на даний крок: {output}")
    print("-" * 50)
print(f"Сума кубів дорівнює {output}\n\n")
print("-" * 50)

# варіант для циклу for:
print("FOR")
output = 0
num = int(input("Введіть будь-яке число: "))
for i in range(1, num+1):
    if i % 3 == 0:
        print(f"Число {i} кратне 3, тому воно пропускається.")
        continue
    output += i ** 3
    print(f"Число, яке має підноситися до степеня: {i}")
    print(f"Сума на даний крок: {output}")
    print("-" * 50)
print(f"Сума кубів дорівнює {output}\n\n")
