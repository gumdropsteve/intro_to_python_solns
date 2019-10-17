vocabulary = set()

while True:
    word = input('Enter a word to add to the vocabulary: ')
    if word == 'q':
        break
    if word == 'v':
        print(' '.join(vocabulary))
    else:
        vocabulary.add(word)
