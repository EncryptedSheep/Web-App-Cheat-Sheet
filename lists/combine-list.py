#!/usr/bin/python

import sys

if len(sys.argv) < 3:
    print " [*] Usage: combine-list.py <wordlist1.txt> <wordlist2.txt> <output.txt> "
    sys.exit()

wl1 = sys.argv[1]
wl2 = sys.argv[2]
out = sys.argv[3]
i=0
words1 = []
words2 = []
wordsAll = []

with open(wl1,'r') as data1:
    for line in data1:
        words1.append(line.rstrip('\n'))

with open(wl2,'r') as data2:
    for line in data2:
        words2.append(line.rstrip('\n'))

for word1 in words1:
    wordsAll.append(word1)

for word2 in words2:
    wordsAll.append(word2)

for word1 in words1:
    for word2 in words2:
        wordsAll.append(str(word1)+str(word2))

with open(out,'w') as output:
    for item in wordsAll:
        output.write(item+'\n')

print ' [*] Wordlist 1: %d' % (len(words1))
print ' [*] Wordlist 2: %d' % (len(words2))
print ' [*] Combinations made: %d' % (len(wordsAll))
print ' [*] Output written to: %s\n' % (out)


