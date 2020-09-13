import random

def get_words_from_file(text_file):

    with open(text_file, "r", encoding='utf-8') as f:
        data = f.read()
        return data


def get_random_sentence(num, word_list):

    data = get_words_from_file("text.txt")
    word_list = []
    for i in range(num):
        word_list.append(random.choice(data.split()))
    return" ".join(word_list)


def main():

    print("Function print a sentence comprised of all the words whose letters equal the number you typed in \n")
    number = int(input("Please type a number between 2 and 20"))

    word_list = get_words_from_file('text.txt')
    sentence = get_random_sentence(number, word_list)
    print(sentence)


if __name__ == '__main__':
    main()
    





