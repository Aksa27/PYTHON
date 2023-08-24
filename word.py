def count_word(sentence):
    words=sentence.split()
    return len(words)
input_sentence=input("enter the sentence:")
count_word=count_word(input_sentence)
print("number of words:",count_word)