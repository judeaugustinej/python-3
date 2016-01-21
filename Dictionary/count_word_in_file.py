"""
Count the occurance of word in any given
file, and store the data in dictionary.
"""
import sys
import os

fname = raw_input('Enter the file name: ')

if not os.path.exists(fname):
    print("Enter a valid file name")
    sys.exit()

word_count = dict()
with open(fname) as fp:
    for line in fp:
        line.strip()
        line = line.split()
        for word in line:
            word_count[word] = word_count.get(word,0) + 1
print(word_count)
