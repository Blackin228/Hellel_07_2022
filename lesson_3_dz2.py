input_list = input("Please enter any string:  ")
input_list = input_list.upper()

first_list = input_list[0::2]
second_list = input_list[-1::-1]

print("Even characters from a string: ", first_list)
print("Сharacters from the string in reverse order: ", second_list)
