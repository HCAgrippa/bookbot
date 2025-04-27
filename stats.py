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

def get_sorted_char_list(char_dic):
    sorted_char_list = []
    for char in char_dic:
        if char.isalpha and char != " " and char != "\n":
            sorted_char_list.append({"char": char, "num": char_dic[char]})
    def sort_key(dic):
        return dic["num"]
    sorted_char_list.sort(reverse=True, key=sort_key)
    return sorted_char_list
