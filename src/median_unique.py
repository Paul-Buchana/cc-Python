# -*- coding: cp1252 -*-
# Author: Paul Buchana
# E-Mail: pbuchana@andrew.cmu.edu
# Last Modified: 14th/June/2014

# This implementation calculates the median number of unique words per tweet. 
# For each tweet, the median is updated.


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––

fin = open('C:\\Users\\pbuchana\\Dropbox\\cc-Python\\tweet_input\\tweets.txt', 'rU')

try:
    # Creating a list to store the number of unique words per tweet.
    uniqueWordsCount = []
    # Extracting tweets from the file object fin.
    for tweet in fin:
        # Creating a list to store unique words per tweet. 
        uniqueWords = []
        for uniqueWord in tweet.split():
            if not uniqueWord in uniqueWords:
                uniqueWords.append(uniqueWord)
        uniqueWordsCount.append(len(uniqueWords))
        
finally:
    # Closing the file object.
    fin.close()

# Function that computes the cummulative sum of a list of numbers.
# Alternstive is the cumsum function built into the numpy library.
def cumsum(numlist):
    total = 0
    for num in numlist:
        total +=num
        yield total

# Computing the median.
median = []
for index, item in enumerate(cumsum(uniqueWordsCount)):
        newMedianValue = item/(index+1.0)
        median.append(newMedianValue)

# Writting the Median to a text file.
with open ('C:\\Users\\pbuchana\\Dropbox\\cc-Python\\tweet_output\\ft1.txt', 'w') as fout:
    for medianValue in median:
        fout.write("%s\n" % medianValue)
