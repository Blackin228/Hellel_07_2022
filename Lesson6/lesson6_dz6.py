import random


def create_num():
    low_num = int(input("Ввведіть нижнє значення інтервалу: "))
    high_num = int(input("Введіть верхнє значення інтервалу: "))
    comp_num = random.randint(low_num, high_num+1)
    return comp_num


def input_num():
    while True:
        user_num = input("Введіть число яке на вашу думку буде правильним: ")
        if not user_num.isdigit():
            print("Ви ввели не число, введіть число")
        else:
            break
    user_num = int(user_num)
    return user_num


def check(comp_num):
    while True:
        user_num = input_num()
        if user_num == comp_num:
            print("Вітаю, ви ввели правильне число")
            break
        elif user_num > comp_num:
            print("Число більше загаданого, спробуйте ще раз")
        else:
            print("Число менше загаданого, спробуйте ще раз")


def main():
    comp_num = create_num()
    check(comp_num)


main()
