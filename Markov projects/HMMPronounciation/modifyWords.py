import re

lines = open('syllableSortedWords.txt').readlines()
syllables = open('SyllableWords.txt').read().split('\n')
f = open('syllWords.txt','w')
for line in lines:
    if line.strip().split(' ')[0].lower() in syllables:
        f.write(line)

f.close()