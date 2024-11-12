import random
from nltk.corpus import words
import nltk

# Download the words corpus if you haven't already
nltk.download("words")

word_list = words.words()
for word in word_list:
    with open("random_words.txt", 'a', encoding='utf-8') as file:
        file.write(word + "\n")
random_word = random.choice(word_list)
print(random_word)
