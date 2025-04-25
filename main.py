def get_book_text(bookfile):
    with open(bookfile) as f:
        book_contents = f.read()
        return book_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

main()
