"""class: Classes are a user-defined data type that is used to encapsulate data and associated functions together. It also helps in binding data together into a single unit.
Data Member: A variable or memory location name that holds value to does a specific task within a program.
Member Function: They are the functions, usually a block of a code snippet that is written to re-use it.
Instance variable: A variable that is defined inside a method of a class.
Function Overloading: This technique is used to assign multiple tasks to a single function, and the tasks are performed based on the number of arguments or the type of argument the function has.
Operator Overloading: It is the technique of assigning multiple functions/tasks to a particular operator.
Inheritance: It is the process of acquiring the properties of one class to another, i.e., one class can acquire the properties of another.
Instantiation: It is the technique of creating an instance of a class."""

import random
from urllib.request import URLopener, urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
        "class %%%(%%%):":
            "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)" :
            "class %%% has-a __init__ that takes self and *** params.",
        "class %%%(object) :\n\tdef ***(self, @@@)":
            "class has-a function *** that takes self and @@@ params.",
        "*** = %%%()":
            "Set *** to an instance of class %%%.",
        "***.***(@@@)":
            "From *** get the *** function, call it with params self, @@@.",
        "***.*** = '***'": 
            "From *** get the *** attribute and set it to'***'."  
}


# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        #fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake parameter lists
        for word in param_names:
            result = result.replace("***", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"answer: {answer}\n\n")
except EOFError:
    print("\Bye")        