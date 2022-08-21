
for i in range(0, 2):
    sign = lambda x: print("Число парне") if (x % 2 == 0) else print("Число непарне")

    num = int(input("Введіть будь-яке число:  "))

    sign(num)
