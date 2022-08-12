# start = 1
# output = 0
# num = int(input("Введіть будь-яке число: "))
# while start <= num:
#     if start % 3 == 0:
#         continue
#     output += start ** 3
#     start += 1
#     print(output)

i = 1
num = int(input("Please enter any number: "))
while i <= num:
    if i % 3 == 0:
        continue
    print(i)
    i += 1
