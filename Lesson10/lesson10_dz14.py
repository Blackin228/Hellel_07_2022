line = b'r\xc3\xa9sum\xc3\xa9'
line_str = line.decode()

print("Початковий рядок у байтовому вигляді: ", line)
print("Декодований рядок: ", line_str)

line_latin1 = line_str.encode('Latin1')
print("Рядок у байтовому представлені у кодуванні Latin1: ", line_latin1)

line_latin1_str = line_latin1.decode('Latin1')
print("Декодований рядок з кодування Latin1: ", line_latin1_str)

