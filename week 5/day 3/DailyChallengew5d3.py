class Palindrome():

    def checker(word):
        reverse = word[::-1]
        if word == reverse:
            return True
        else:
            return False     


word = Palindrome.checker("word")
print(word)            