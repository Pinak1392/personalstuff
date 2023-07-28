import re

REGEXP = re.compile(r'[^:]+')

string = 'root:x:0:1:Super-User:/:/sbin/sh'

m = REGEXP.findall(string)

print(m)