def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    word_count = get_word_count(text)
    print(f"Word count: {word_count}")


def get_word_count(string):
    words = string.split()
    return len(words)


def get_book_path(path):
    with open(path) as f:
        return f.read()


main()
