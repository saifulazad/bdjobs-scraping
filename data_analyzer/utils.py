
def get_non_dict_word(words_set):
    with open('./words.txt') as word_dictionary:
        dict_words = {x.rstrip().lower() for x in word_dictionary.readlines()}

        non_word = words_set - (dict_words & words_set)
        return non_word