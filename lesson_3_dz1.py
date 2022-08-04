print("Three variables")
print("*" * 50)
# три однакових змінні з однаковими id:
var_1 = 50
var_2 = 50
var_3 = 50
print("var_1 = ", var_1)
print("var_2 = ", var_2)
print("var_3 = ", var_3)
# перевірка:
print("Check: ")
print("var_1 == var_2 == var_3 :", var_1 == var_2 == var_3)
print("var_1 is var_2 is var_3 :", var_1 is var_2 is var_3)
# зміна на неоднакові id:
var_1 = float(var_1)
var_2 = int(var_2)
var_3 = float(var_3)
# перевірка:
print("Checking changed variables: ")
print("var_1 == var_2 == var_3 :", var_1 == var_2 == var_3)
print("var_1 is var_2 is var_3 :", var_1 is var_2 is var_3)
print("*" * 50)
print("\n" * 2)
print("Two variables")
print("*" * 50)
# дві змінні
var_1 = [21, 45, 'text']
var_2 = [21, 45, 'text']
print("var_1 = ", var_1)
print("var_2 = ", var_2)
# перевірка:
print("Check: ")
print("var_1 == var_2 :", var_1 == var_2)
print("var_1 is var_2 :", var_1 is var_2)
# зміна на однакові id:
var_1 = bool(var_1)
var_2 = bool(var_2)
# перевірка:
print("Checking changed variables: ")
print("var_1 == var_2 :", var_1 == var_2)
print("var_1 is var_2 :", var_1 is var_2)
print("*" * 50)

