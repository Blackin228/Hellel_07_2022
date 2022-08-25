input_data = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']
output_data = list(filter(lambda x: x if x == x[-1::-1] else 0, list(map(str.lower, input_data))))
print(f"Надані Слова: {input_data}")
print(f"Слова поліндроми: {output_data}")
