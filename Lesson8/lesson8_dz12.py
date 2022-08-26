from datetime import datetime


def my_decorator(func):
    def count():
        time_1 = datetime.now()
        func()
        time_2 = datetime.now()
        print("Time of working program: ", time_2 - time_1)
    return count


@my_decorator
def output_1():
    nickname = input("Please enter your nickname: ")
    print(f"Hello, {nickname}")


@my_decorator
def output_2():
    age = input("Please enter your age: ")
    print(f"I am is {age} yars old.")


output_1()
print("-" * 50)
output_2()
