sentence = input("Please type a sentence. ")
letter = input("Please type letter. ")
def count_let(sentence, letter):
    counter = 0
    for words in sentence:
        for let in words:
            if let == letter:
                counter +=1
    return counter
let_count = count_let(sentence,letter)
print(let_count)
