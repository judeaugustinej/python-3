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
"""
Enter the file name: romeo.txt
{'and': 3, 'envious': 1, 'already': 1, 'fair': 1, 'is': 3, 'through': 1,
'pale': 1, 'yonder': 1, 'what': 1, 'sun': 2, 'Who': 1, 'But': 1, 'moon': 1,
'window': 1, 'sick': 1, 'east': 1, 'breaks': 1, 'grief': 1, 'with': 1, 'light': 1,
'It': 1, 'Arise': 1, 'kill': 1, 'the': 3, 'soft': 1, 'Juliet': 1}
"""
