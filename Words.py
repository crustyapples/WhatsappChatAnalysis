import re
from operator import itemgetter


class Word:
    def __init__(self, text):
        self.text = text

    def Count(self, word_length, list_length):
        self.word_length = word_length
        self.list_length = list_length

        word_script = ' '.join(self.text)
        pattern = '[a-z]{%s,}' % word_length
        word_search = re.compile(pattern)
        word_list = word_search.findall(word_script)
        count = {}

        for msg in word_list:
            count.setdefault(msg, 0)
            if msg in word_list:
                count[msg] += 1

        tuple_list = count.items()
        sorted_list = sorted(tuple_list, key=itemgetter(1), reverse=True)
        final_list = sorted_list[:list_length]
        for i in range(len(final_list)):
            print(str(final_list[i][0]) + ' = ' + str(final_list[i][1]))
