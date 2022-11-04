dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'frog', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")