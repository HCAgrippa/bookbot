from stats import get_word_num, get_char_count, get_sorted_char_list


def main():
    book = get_book_text("books/frankenstein.txt")
    words = get_word_num(book)
    char_dic = get_char_count(book)
    sorted_char_list = get_sorted_char_list(char_dic)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {words} total words\n--------- Character Count -------")
    for dic in sorted_char_list:
        char = dic["char"]
        num = dic["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

def get_book_text(bookfile):
    with open(bookfile) as f:
        book = f.read()
        return book


main()
