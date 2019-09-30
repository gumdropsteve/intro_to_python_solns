word_dict = {}
while True:
    entry = input('Please enter a coordinate-word pair in the format (x, y, word): ')
    if not entry:
        break
    x, y, word = entry.split(', ')
    word_dict[(x, y)] = word

while True:
    lookup = input('Please enter a coordinate to look up: ')
    if lookup == 'q':
        break
    coord = tuple(lookup.split(', '))
    if coord not in word_dict:
        print('Coordinate not found')
        continue
    print(word_dict[coord])
