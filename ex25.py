def break_words(stuff):
    """This function breaks up workds into an array"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """prints the first words after popping off"""
    word = words.pop(0)
    print(words)

def print_last_word(words):
    """Prints the last word after poppung it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one"""
    words = sort_sentence(words)
    print_first_word(words)
    print_last_word(words)