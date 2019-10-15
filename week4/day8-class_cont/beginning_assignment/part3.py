def count_words(book_path):
    '''
    Input:  Str - file path to book location.

    Makes for easy way to count words in a book .txt file.
    '''
    num_words = 0
    with open(book_path) as book:
        for line in book:
            num_words += len(line.split())
    return num_words

if __name__ == '__main__':
    flat_land_counts = count_words('books/flatland.txt')
    print(flat_land_counts)
    programming_lang_counts = count_words('books/programming_languages.txt')
    print(programming_lang_counts)
