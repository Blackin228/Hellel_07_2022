class String(object):

    def __init__(self, line):
        self.line = str(line)

    def __add__(self, other):
        if type(other) == String:
            return self.line + other.line
        else:
            return self.line + str(other)

    def __sub__(self, other):
        if not self.line.find(str(other)):
            return self.line
        else:
            return self.line.replace(str(other), '', 1)


print(String('New') + String(890))
print(String(1234) + 5678)
print(String('New') + 'castle')
print(String('New') + 77)
print(String('New') + True)
print(String('New') + ['s', ' ', 23])
print(String('New') + None)

print("-" * 50)

print(String('New bala7nce') - 7)
print(String('New balance') - 'bal')
print(String('New balance') - 'Bal')
print(String('pineapple apple pine') - 'apple')
print(String('New balance') - 'apple')
print(String('NoneType') - None)
print(String(55678345672) - 7)
