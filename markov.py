"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_text = open(file_path).read()

    return file_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    # split file text into individual words 
    words = text_string.split()
    # loop by index through every 2 word pairs in word list (ending is length of word list - 2)
    for i in range(len(words) - 2):
        key = (words[i], words[i+1])
        value = words[i+2]
        
        if key not in chains:
            chains[key] = []
        
        chains[key].append(value)
        # create tuple of 2 word pair
        # add tuple to dictionary as key
        # based on tuple just added, update value to list for that tuple

    return chains


def make_text(chains):
    """Return text from chains."""
    #grab a random tuple
    all_keys = list(chains.keys())
    curr_key = choice(all_keys)
    # initialize words list and populate with first tuple 
    words = [curr_key[0], curr_key[1]]

    # this will stop when we get a two word combo that is not a key
    while curr_key in chains:
        #choose random word from values for curr_key
        curr_word_options = chains[curr_key]
        curr_word = choice(curr_word_options)

        #add word to words_list
        words.append(curr_word)

        #create new tuple and go back
        curr_key = (curr_key[1], curr_word)

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
