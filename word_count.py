# put your code here.
import sys


def count_words(filename):
    """Returns dictionary with words as keys, and word count as value"""
    data = open(filename)
    word_count = {}

    for line in data:
        string = line.rstrip()
        words = string.split(" ")

        for word in words:
            clean_word = word.rstrip(",").rstrip(".").lower()
            word_count[clean_word] = word_count.get(clean_word, 0) + 1

    return word_count


def key_value_pairs(filename, word=" "):
    """Returns how many times this word appears in file"""

    our_count = count_words(filename)
    for word, count in our_count.iteritems():
        print word, count

    # The code below will look for count of specific key
    # my_count = our_count.get(word, 0)
    # return my_count

for i in range(1, len(sys.argv)):
    total_count = key_value_pairs(sys.argv[i])