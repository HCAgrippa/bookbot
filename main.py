from stats import get_word_num
from stats import get_char_count

def main():
    book = get_book_text("books/frankenstein.txt")
    words = get_word_num(book)
    print(f"{words} words found in the document")
    char_dic = get_char_count(book)
    print(char_dic)
#    for char in char_dic:
#        print(f"{char}: {char_dic[char]}")

def get_book_text(bookfile):
    with open(bookfile) as f:
        book = f.read()
        return book

main()
