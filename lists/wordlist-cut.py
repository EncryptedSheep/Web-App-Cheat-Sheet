#!/usr/bin/python

import sys

if len(sys.argv) < 3:
    print " [*] Usage: wordlist-cut.py <wordlist.txt> <start num> <output.txt> "
    sys.exit()

wl = sys.argv[1]
start = int(sys.argv[2])
out = sys.argv[3]
i=0
words = []

with open(wl,'r') as data:
    for line in data:
        i+=1
        if i >= start:
            words.append(line.rstrip('\n'))

with open(out,'w') as output:
    for item in words:
        output.write(item+'\n')

print ' [*] Words found: %d' % (len(words))
print ' [*] Output written to: %s\n' % (out)

