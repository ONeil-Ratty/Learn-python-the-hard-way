import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.or/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%)" : 
    "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__self(self, ***)" :
    "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function named *** that takes self and @@@ parameters",
    "*** = %%%()":
    "From *** get the *** function, and call it with parameters self, @@@",
    "***.*** = '***":
    "From *** get the *** attribute and set it ro '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.apppend(word.strip())

def convert(snippet, phrase):
    class_names = [w.capalize() for w in
                   random.sample(WORDS,snippet.count('%%%'))]
    other_names = random.sample(WORDS,snippet.count('%%%'))
    results = []
    param_names = []

    for i in range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        results = sentence[:]

        #fake class names
    for word in class_names:
        results = results.replace("%%%",word,1)

        #fake other names
    for word in other_names:
        results = results.replace("***",word,1)

        #fake parameter lists
    for word in param_names:
        results = results.replace("@@@",word,1)

    results.append(results)
    
    return results

# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question,answer = convert(snippet,phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input('> ')
            print(f"Answer: {answer}")

except EOFError:
    print("\nBye")

