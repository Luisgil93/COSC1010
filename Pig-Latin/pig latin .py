#
# Name luis
# Date 11/10/2024
# Pig Latin Programming Project
# COSC 1010
#
# User enters sentence they want to convert.
sentence = input("Enter a sentence:")
words = sentence.split()

pig_latin_words = []
for word in words:
    pig_latin_word = word[1:] + word[0] + "ay"

    pig_latin_words.append(pig_latin_word)
pig_latin_sentence = " ".join(pig_latin_words)
# The sentence converted 
print("Pig latin: ", pig_latin_sentence)