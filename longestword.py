def longest_words(sentence):
    words=sentence.split()
    longest_word=max(words,key=len)
    return longest_word
input_sentence=input("enter the sentence:")
longest_word=longest_words(input_sentence)
print("the longest word is:",longest_word)