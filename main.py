import sys
from stats import (
    get_word_num,
    get_char_count,
    get_sorted_char_list
)


def main():
    check_arguments()
    path = sys.argv[1]
    book = get_book_text(path)
    words = get_word_num(book)
    char_dic = get_char_count(book)
    sorted_char_list = get_sorted_char_list(char_dic)
    report(path, words, sorted_char_list)


def check_arguments():
    try:
        return sys.argv[1]
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(bookfile):
    with open(bookfile) as f:
        book = f.read()
        return book


def report(path, words, sorted_char_list):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------\nFound {words} total words\n--------- Character Count -------")
    for dic in sorted_char_list:
        char = dic["char"]
        num = dic["num"]
        print(f"{char}: {num}")
    print("============= END ===============")


main()
