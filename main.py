from stats import get_word_num

def main():
    book = (get_book_text("books/frankenstein.txt"))
    words = (get_word_num(book))
    print(f"{words} words found in the document")

def get_book_text(bookfile):
    with open(bookfile) as f:
        book = f.read()
        return book

main()
