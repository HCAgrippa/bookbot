def get_word_num(book):
     return len(book.split())

def get_char_count(book):
     lc_book = book.lower()
     char_dic = {}
     for char in lc_book:
         if char in char_dic:
             char_dic[char] += 1
         else:
             char_dic[char] = 1
     return char_dic

