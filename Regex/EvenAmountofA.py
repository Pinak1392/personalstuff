import re

inp = input('Gimme them A\'s: ')

REG = re.compile(r'^(?=[^a]*(?:[^a]*a[^a]*a)*[^a]*$)')

print(REG.match(inp))