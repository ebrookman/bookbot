from stats import get_num_words
from stats import get_num_characters
from stats import get_report
import sys

# read the book text into a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    character_set = get_num_characters(book_text)
    sorted_list = get_report(character_set)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for item in sorted_list:
        if item.keys():
            key = list(item.keys())[0]
            value = list(item.values())[0]
            if key.isalpha():
                print(f"{key}: {value}")
    print("============= END =============")


main()


