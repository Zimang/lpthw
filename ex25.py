def break_words(stuff):
    """这个函数切割字符"""
    words = stuff.split(" ")
    return words


def sort_words(words):
    """为字符列表排序"""
    return sorted(words)


def print_first_word(words):
    """打印并弹出第一个字符"""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """打印并弹出最后一个字符"""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """打断字符串，排序"""
    words = sentence.spilt(" ")
    return sort_words(words)


def print_first_and_last(sentence):
    """打印首尾字符"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
