import math


class NegativeDegreeException(Exception):
    pass


class Calc(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return """Дана програма є примітивним калькулятором
Ви можете провести додавання(1), віднімання(2), ділення(3),
множення(4), піднесення до степення(5), Знаходження корення квадратного з числа(6)"""

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def div(self):
        try:
            result = self.x / self.y
        except ZeroDivisionError:
            result = "На нуль ділити не можна"
        return result

    def mul(self):
        return self.x * self.y

    def pow(self):
        try:
            if self.y < 0:
                raise NegativeDegreeException
            else:
                return self.x ** self.y
        except NegativeDegreeException:
            return "Ви хочете піднести число у відємний степінь"

    def sqrt(self):
        try:
            result = math.sqrt(self.x)
        except ValueError:
            result = "З від'ємного числа не можна знайти корінь квадратний"
        return result


print(Calc())
print("Щоб вийти введіть 0")
while True:
    sel = int(input("Введіть що ви хочете зробити з числами: "))
    if sel == 0:
        break
    x = int(input("Введіть перше число: "))
    try:
        y = int(input("Введіть друге число: "))
    except ValueError:
        if sel == 6:
            y = 0
        else:
            print("Ви ввели некоректне значення")
            continue
    finally:
        a = Calc(x, y)
    if sel == 1:
        print("Відповідь: ", a.add())
    elif sel == 2:
        print("Відповідь: ", a.sub())
    elif sel == 3:
        print("Відповідь: ", a.div())
    elif sel == 4:
        print("Відповідь: ", a.mul())
    elif sel == 5:
        print("Відповідь: ", a.pow())
    elif sel == 6:
        print("Відповідь: ", a.sqrt())
    print("-" * 50)
