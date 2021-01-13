"""Generate Markov text from text files."""

import sys
from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_text = open(file_path).read()

    return file_text


def make_chains(text_string, ngram_size):
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
    # loop by index through every ngram_size word pairs in word list (ending is length of word list - ngram_size)
    print(len(words))
    for word_idx in range(len(words) - ngram_size):
        # Create tuple for key
        temp_key = [words[word_idx]]
        for offset in range(1, ngram_size):
            # we don't know the size of our tuple so we create a list first
            temp_key.append(words[word_idx + offset])

        # set fully populated temp_key value to key as tuple
        key = tuple(temp_key)
        # get word to add to chains dictionary as value for this key
        value = words[word_idx + ngram_size]
        
         # add tuple to dictionary as key, if not already there
        if key not in chains:
            chains[key] = []
        
        # based on tuple just added, update value to list for that tuple
        chains[key].append(value)
       
    return chains


def make_text(chains, ngram_size):
    """Return text from chains."""
    #grab a random tuple
    all_keys = list(chains.keys())
    curr_key = choice(all_keys)

    # initialize words list and populate with first tuple 
    words = [curr_key[0]]
    # Because we do not know the size of the key, we loop through
    for i in range(1, ngram_size):
        words.append(curr_key[i])

    # this will stop when we get a n word combo that is not a key
    while curr_key in chains:
        #choose random word from values for curr_key
        curr_word_options = chains[curr_key]
        curr_word = choice(curr_word_options)

        #add word to words_list
        words.append(curr_word)

        #create new tuple and go back
        curr_key = list(curr_key[1:])
        curr_key.append(curr_word)
        curr_key = tuple(curr_key)

    return ' '.join(words)

# if user gives different file name when running program, use that
input_path = 'green-eggs.txt' if len(sys.argv) == 1 else sys.argv[1]
n = 2 if len(sys.argv) <= 2 else int(sys.argv[2])

print(input_path)

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print(random_text)