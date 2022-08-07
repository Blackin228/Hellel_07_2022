
two_words = input("Please enter two words separated by a space: ")
two_words_ = two_words.split(" ")
first_word = two_words_[0][-1::-1].upper()
second_word = two_words_[1][-1::-1].title()

output_1 = "!First word: %s, Second word: %s ?" % (first_word, second_word)
output_2 = "!First word: {}, Second word: {} ?".format(first_word, second_word)
output_3 = f"!First word: {first_word}, Second_word: {second_word} ?"

words_file = open("text.txt", "w")

print(two_words, output_1, output_2, output_3, sep="<<<>>>", file=words_file)

words_file.close()
