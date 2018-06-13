# Planet_anagrams

'''This script takes in a text file of words expected to be located in '/usr/share/dict/words' or '/usr/dict/words', and output all the anagrams that are both more than 4 letters and have more annagrams than letters in that list
This is accomplished by converting each letter into a prime number, then making each word a product (word_id) of primes which is unique for each set of anagrams
Once the word_id has been created, a dictionary is made of each word_id and associated words (anagrams) then outputs the filterd list based on the given criteria.'''

