def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    sorted_letter_count = get_sorted_letter_count(letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"Number of words found in the document: {word_count}\n")
    print_letter_count(sorted_letter_count)
    print("\n--- End report ---")


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


def get_sorted_letter_count(dict):
    only_letters = {}
    for key, value in dict.items():
        if key.isalpha():
            only_letters[key] = value

    sorted_tuples = sorted(only_letters.items(), reverse=True, key=lambda item: item[1])
    return sorted_tuples


def print_letter_count(list):
    for i in range(0, len(list)):
        print(f"The letter {list[i][0]} was found {list[i][1]} times.")


main()