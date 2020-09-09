word = input("Please type ten lettered word.")
print(word[0], word[9])
for i in range(11):
    print(word[0:i:1])
from random import shuffle
word = list(word)
shuffle(word)
print(''.join(word))