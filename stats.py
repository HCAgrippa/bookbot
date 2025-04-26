def get_word_num(book):
     return len(book.split())

def get_char_count(book):
     lc_book = book.lower()
     char_dic = {}
     char_set = set()
     for char in lc_book:
         if char in char_set:
             char_dic[char] += 1
         else:
             char_set.add(char)
             char_dic[char] = 1
     return char_dic

