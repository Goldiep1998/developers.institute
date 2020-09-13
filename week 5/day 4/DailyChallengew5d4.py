import re
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize

class Text():

    def __init__(self, text):
        self.text = text.lower()
        self.most_used_word = None
        self.unused_words = None

    @staticmethod
    def from_file(file_path):
        with open(file_path, "r") as f:
            file_text = f.read()
        return Text(file_text)

    def words_usage(self, word):
        return self.text.split(" ").count(word)

    def most_used(self):
        if self.most_used_word:
           return self.most_used_word
        else:
           words = {}
           for word in self.text.split(" "):
               if word in words:
                   words[word] += 1
               else:
                   words[word] = 1

           count = 0
           word = ""
           for key, value in words.items():
               if value > count:
                   count = value
                   word = key
           self.most_used_word = word, count
           return self.most_used_word

    # def seldom_used(self):
    #     if self.unused_words:
    #         return self.unused_words
    #     else:
    #         words{}
    #         for word in self.text.split(" "):


class TextModification(Text):

    def without_punctuation(self):
        res = re.sub(r'[^\w\s]', '', self.text)
        print(res)

    def remove_stop_words(self):
        text_tokens = word_tokenize(self.text)
        filter_sentence = [word for word in text_tokens if not word in stopwors.word()]
        print(filter_sentence)




t = Text.from_file('the_stranger.txt')
TextModification.without_punctuation()