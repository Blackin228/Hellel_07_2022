input_list=input("Please enter any string:  ")
input_list=input_list.upper()

first_list=list(input_list[0::2])
second_list=list(input_list[-1::-1])

print(first_list)
print(second_list)
