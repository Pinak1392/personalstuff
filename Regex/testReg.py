import re

with open('words.txt') as f:
    for l in f:
        #Everything with 3 letters
        if re.search(r'^.o.o$',l.strip()):
            print(l.strip())