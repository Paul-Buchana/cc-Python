# -*- coding: cp1252 -*-
# Author: Paul Buchana
# E-Mail: pbuchana@andrew.cmu.edu
# Last Modified: 14th/June/2014

# This implementaion takes in a text file containing tweets and
# perfoms a count of unique words therein.


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––

import collections

fin = open('C:\\Users\\pbuchana\\Dropbox\\cc-Python\\tweet_input\\tweets.txt', 'rU')
try:
    # Tweet words list container.
    tweetWords = []
    # Iterating through each line(tweet) in the text file.
    for tweet in fin:
        # Extracting the words per tweet and adding them to tweetWords array.
        for word in tweet.split():
            tweetWords.append(word)
finally:
    fin.close()

# Collecting unique words and adding them to uniqueWords list.
uniqueWords = []
for uniqueWord in tweetWords:
    if not uniqueWord in uniqueWords:
          uniqueWords.append(uniqueWord)

# Perorming a unique word cout. Storing result in a dictionary.
uniqueWordCount = {}
for word in uniqueWords:
    uniqueWordCount[word] = tweetWords.count(word)

# Sorting the dictionary by key.
uniqueWordCount = collections.OrderedDict(sorted(uniqueWordCount.items()))

# Writting the Key value pairs to an output file.
with open ('C:\\Users\\pbuchana\\Dropbox\\cc-Python\\tweet_output\\ft2.txt', 'w') as fout:
    for pair in uniqueWordCount.items():
        fout.write("%s %s\n" % pair)
