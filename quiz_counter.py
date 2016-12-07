import random
from urllib import urlopen
import sys

import ex26
WORD_SOURCE = open("random_word_list.txt", 'r')
word_list = []
print word_list
# word_list = [line.strip().split(' ') for line in WORD_SOURCE.readlines()]
fu = "This\nis\nmy\nlife."
fu.strip('\n')
print fu
for line in WORD_SOURCE.readlines():
    line.strip("\n")
    word_list.append(line)
print word_list
# print word_list
#
# boo = word_list
# boo.strip().split(' ')
# print "++++++++++++", boo
# tct = open(random_word_list)
# print WORD_SOURCE.readlines()
# for worda in WORD_SOURCE.readlines():
#     world_list.append([worda])
# word_list.append(WORD_SOURCE.readlines)

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


# WORD_SOURCE.break_words(loo)
# print WORD_SOURCE
# for word in WORD_SOURCE.readlines():
#     word_list.append(words)
# # print WORD_SOURCE
# ex26.break_words(W)


WORD_URL = "http://learncodethehardway.org/words.txt"

answer_count = 0
bad_count = 0

WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%",
    "***.***(@@@)":
        "From *** get the *** function, call it with parameters self, @@@",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
# for word in open('random_word_list.txt').readlines():
#     WORDS.append(word.strip())

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            print question

            raw_input("\n   >>   ")
            print "\nANSWER: %s\n\n" % answer
            answer = raw_input(". .\t Was it Right? y/n > ")

            if answer == "y":
                answer_count += 1
            else:
                bad_count += 1
            print "Yes: %i and No: %i" % (answer_count, bad_count)

except EOFError:
    print "\nBye\n"
