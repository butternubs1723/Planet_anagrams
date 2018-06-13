#!/usr/bin/env python

'''This script takes in a text file of words expected to be located in '/usr/share/dict/words' or '/usr/dict/words', and output all the anagrams that are both more than 4 letters and have more annagrams than letters in that list
This is accomplished by converting each letter into a prime number, then making each word a product (word_id) of primes which is unique for each set of anagrams
Once the word_id has been created, a dictionary is made of each word_id and associated words (anagrams) then outputs the filterd list based on the given criteria.'''

import sys
import string
import os

#creates a dictionary that relates alphabet characters to numbers {a:2, A:2, b:3, B:3...z:101,Z:101}
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
          47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
letter_id = dict(zip(string.ascii_lowercase, primes))
letter_upper = dict(zip(string.ascii_uppercase, primes))
letter_id.update(letter_upper)

def locate_anagrams(word_list):
    #anagrams = {product:[#_letters, #anagrams, anagram1, anagram2, etc.], ...}
    anagrams = {}
    previous_word = " "
    #list of words containing non-ascii characters
    non_ascii_words= []
    for word in word_list:

        #avoids making anagrams from duplicate words with "'s" as suffix
        if word[:-2] == previous_word:
            next

        [word_id, key_error] = get_word_id(word)

        #see get_word_id
        if key_error == 1:
            non_ascii_words.append(word)

        elif word_id in anagrams:

            #avoids making anagrams from duplicate words over Upper/lower case i.e. "Ares" vs "ares"
            if string.upper(word[0])+word[1:] in anagrams[word_id]:
                next

            else:
                anagrams[word_id][1] += 1
                anagrams[word_id].append(word)

        else:
            anagrams[word_id]=[len(word), 1, word]

    previous_word = word

    return anagrams, non_ascii_words

def get_word_id(word):
    product = 1
    #key_error is used to check for non ascii characters in word
    key_error = 0

    for letter in word:
        try:
            product *= letter_id[letter]
        except KeyError:
            key_error = 1
    return [product, key_error]

def load_word_list_from_arg(filename):

    f = open(filename)
    word_list = f.read().splitlines()
    return word_list

def filename_exists_check():
    
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        return sys.argv[1]
    else:
        print 'File does not exist.'
        print 'Expected:'
        print '/usr/share/dict/words'
        print 'or'
        print '/usr/dict/words'
        sys.exit()

if __name__ == '__main__':
    
    filename = filename_exists_check()
    
    word_list = load_word_list_from_arg(filename)

    anagrams, non_ascii_words = locate_anagrams(word_list)

    for key, value in anagrams.items():
      if anagrams[key][0] >= 4 and anagrams[key][1] >= anagrams[key][0]:
         print (",".join(anagrams[key][2:]))
