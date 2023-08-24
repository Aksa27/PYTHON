def upper_words(sentence):
    words=sentence.split()
    for word in words:
        if word[0].isupper():
            print(word)
user_input=input("Enter a sentence:")
upper_words(user_input)
            