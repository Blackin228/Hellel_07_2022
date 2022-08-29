name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
age = input("Please enter your age: ")
hobby = input("Please enter your hobby: ")

txt = open("ID.txt", "w")
txt.write(name + "\n" + surname + "\n")
txt.close()

txt = open("ID.txt", "a")
txt.write(age + "\n" + hobby + "\n")
txt.close()
