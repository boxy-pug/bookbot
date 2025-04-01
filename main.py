from stats import get_word_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_path(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    sorted_letter_count = get_sorted_letter_count(letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    print_letter_count(sorted_letter_count)
    print("\n--- End report ---")


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
        print(f"{list[i][0]}: {list[i][1]}")


main()