from hyphen import Hyphenator

h_en = Hyphenator('en_US')

l = h_en.syllables('spenternet')
print(l)