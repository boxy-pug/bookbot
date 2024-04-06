def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    print(f"Word count: {word_count}\nLetter count: {letter_count}")


def get_word_count(string):
    words = string.split()
    return len(words)


def get_book_path(path):
    with open(path) as f:
        return f.read()
    

def get_letter_count(text):
    lowered_text = text.lower()
    letter_count = {}
    for char in lowered_text:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1
    return letter_count


main()
