'''

IE 246 Homework - 1 Question - 2 Solution by Esrah Zahid (S020289)

'''

################ QUESTION 2 ################

my_string = "in the end it is not the years in your life that count it is the life in your years"
words = my_string.split()

last_word = words[-1]
answer1 = words.index(last_word)+1

first_word = words[0]
answer2 = words[::-1].index(first_word)

answer3 = len(set(words[:-answer2]))

middle_index = len(words) // 2
first_half_words = set(words[:middle_index])
second_half_words = set(words[middle_index:])
answer4 = len(first_half_words.intersection(second_half_words))

sorted_words = sorted(words)
separator_index = (len(sorted_words) - 1) // 2
answer5 = sorted_words[separator_index][0].upper()

print(f"The number of words to be read until the last word of the text is heard for the first time is {answer1}. \
The number of remaining words after the first word is read for the last time is {answer2}. \
The number of different words until we hear the first word for the last time is {answer3}.\
The number of common words used in the first and the second half of the text is {answer4}.\
The letter which separates the first approximate half of the used words from the second approximate\
half when all words that have been used are sorted alphabetically is {answer5}.")
